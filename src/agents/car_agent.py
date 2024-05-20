""" Car agent realization """
import logging
import typing

from src.entities.car_entity import CarEntity
from src.entities.traffic_light_entity import TrafficLightEntity
from .agent_base import AgentBase
from .messages import MessageType, Message


class CarAgent(AgentBase):
    """
    Car agent class
    """
    def __init__(self):
        super().__init__()
        self.entity: CarEntity
        self.name = 'Car Agent'
        self.subscribe(MessageType.NEW_TIME_MESSAGE, self.handle_new_time)

    def handle_new_time(self, message, sender):
        """
        Handle new time message
        :param message:
        :param sender:
        :return:
        """
        data = message.msg_body
        logging.info(f'{self} - received {message}, data - {data}')

    def handle_init_message(self, message, sender):
        """
        Handles initialization message.
        :param message:
        :param sender:
        :return:
        """
        super().handle_init_message(message, sender)
        logging.info(f'{self} - next point: {self.entity.next_point}')
        next_point = self.__get_next_point()
        if not next_point:
            logging.error(f'{self} - next point not found')
            return
        next_point_radius = next_point.radius
        distance = self.entity.init_point.get_distance_to_other(next_point.location)
        if distance > next_point_radius:
            logging.debug(f'{self} - next point too far right now')
            return

        time_to_point = distance / self.entity.speed
        message_data = {
            'car': self.entity,
            'time_to_point': time_to_point,
            'from': self.entity.from_direction
        }
        tl_address = self.dispatcher.reference_book.get_address(next_point)
        message = Message(MessageType.NEW_CAR_MESSAGE, message_data)
        self.send(tl_address, message)

    def __get_next_point(self) -> typing.Optional[TrafficLightEntity]:
        traffic_lights = self.scene.get_entities_by_type('TRAFFIC_LIGHT')
        for traffic_light in traffic_lights:
            if traffic_light.name == self.entity.next_point:
                return traffic_light
        return None

