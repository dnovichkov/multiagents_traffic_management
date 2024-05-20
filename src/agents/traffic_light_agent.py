""" Traffic light agent realization """
import logging
import typing

from .agent_base import AgentBase
from .messages import MessageType, Message
from src.entities.car_entity import CarEntity


class TrafficLightAgent(AgentBase):
    """
    Traffic Light agent class
    """
    def __init__(self):
        super().__init__()
        self.entity: CarEntity
        self.name = 'Traffic Light'
        self.subscribe(MessageType.NEW_TIME_MESSAGE, self.handle_new_time)
        self.subscribe(MessageType.NEW_CAR_MESSAGE, self.handle_new_car)

    def handle_new_time(self, message, sender):
        """
        Handle new time message
        :param message:
        :param sender:
        :return:
        """
        data = message.msg_body
        logging.info(f'{self} - received {message}, data - {data}')

    def handle_new_car(self, message, sender):
        """
        Handle new car message
        :param message:
        :param sender:
        :return:
        """
        data = message.msg_body
        logging.info(f'{self} - received {message}, data - {data}')
