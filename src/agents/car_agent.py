""" Car agent realization """
import logging
import typing

from src.entities.car_entity import CarEntity
from src.entities.traffic_light_entity import TrafficLightEntity
from .agent_base import AgentBase
from .messages import MessageType, Message
from src.utils.point import Point, is_point_between


class CarAgent(AgentBase):
    """
    Car agent class
    """
    def __init__(self):
        super().__init__()
        self.entity: CarEntity
        self.name = 'Car Agent'
        self.subscribe(MessageType.NEW_TIME_MESSAGE, self.handle_new_time)
        self.current_point = Point(0, 0)

    def handle_new_time(self, message, sender):
        """
        Handle new time message
        :param message:
        :param sender:
        :return:
        """
        time_step = message.msg_body.get('time_step')
        logging.info(f'{self} - received {message}')
        from_direction = self.entity.from_direction

        possible_next_point = Point(self.current_point.x, self.current_point.y)
        move_distance = self.entity.speed * time_step
        if from_direction == 'N':
            # From North to South: decrease y-coordinate
            possible_next_point.y -= move_distance
        elif from_direction == 'S':
            # From South to North: increase y-coordinate
            possible_next_point.y += + move_distance
        elif from_direction == 'E':
            # From East to West: decrease x-coordinate
            possible_next_point.x -= move_distance
        elif from_direction == 'W':
            # From West to East: increase x-coordinate
            possible_next_point.x += move_distance

        logging.info(f'{self} {possible_next_point=}')
        next_tl = self.__get_next_traffic_light()
        if not next_tl:
            logging.error(f'{self} - next point not found')
            return
        next_point_radius = next_tl.radius
        distance = self.current_point.get_distance_to_other(next_tl.location)
        if distance > next_point_radius:
            # We need check if step is too large and we intersect with traffic light
            if not is_point_between(self.current_point, possible_next_point, next_tl.location):
                self.current_point = possible_next_point
                return
            logging.info(f'{self} - next point too far right now')
        # Car is located in TL's area
        logging.info(f'{self} - is in traffic light area {next_tl} - {next_tl.location=} {distance=}')
        self.current_point = next_tl.get_possible_point(possible_next_point)
        distance_to_tl = self.current_point.get_distance_to_other(next_tl.location)
        # TODO: Possible, change the speed here?
        time_to_point = distance_to_tl / self.entity.speed
        message_data = {
            'car': self.entity,
            'time_to_point': time_to_point,
            'from': self.entity.from_direction,
            'location': self.current_point,
        }
        tl_address = self.dispatcher.reference_book.get_address(next_tl)
        message = Message(MessageType.NEW_CAR_MESSAGE, message_data)
        self.send(tl_address, message)

    def handle_init_message(self, message, sender):
        """
        Handles initialization message.
        :param message:
        :param sender:
        :return:
        """
        super().handle_init_message(message, sender)
        self.current_point = self.entity.init_point
        logging.info(f'{self} - next point: {self.entity.next_point}')
        next_point = self.__get_next_traffic_light()
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
            'from': self.entity.from_direction,
            'location': self.entity.init_point,
        }
        tl_address = self.dispatcher.reference_book.get_address(next_point)
        message = Message(MessageType.NEW_CAR_MESSAGE, message_data)
        self.send(tl_address, message)

    def __get_next_traffic_light(self) -> typing.Optional[TrafficLightEntity]:
        traffic_lights = self.scene.get_entities_by_type('TRAFFIC_LIGHT')
        for traffic_light in traffic_lights:
            if traffic_light.name == self.entity.next_point:
                return traffic_light
        return None
