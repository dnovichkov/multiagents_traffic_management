""" Car agent realization """
import logging
import typing

from .agent_base import AgentBase
from .messages import MessageType, Message
from src.entities.car_entity import CarEntity


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
