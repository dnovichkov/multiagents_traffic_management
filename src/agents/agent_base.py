import traceback
from typing import Dict, Callable, Any, List
from abc import ABC
import logging

from thespian.actors import Actor, ActorAddress, ActorExitRequest

from .messages import MessageType, Message


class AgentBase(ABC, Actor):
    """
    Base class for agents
    """

    def __init__(self):
        self.name = 'Base Agent'
        super().__init__()
        self.handlers: Dict[MessageType, Callable[[Any, ActorAddress], None]] = {}
        self.scene = None
        self.dispatcher = None
        self.entity = None
        self.subscribe(MessageType.INIT_MESSAGE, self.handle_init_message)

    def subscribe(self, msg_type: MessageType, handler: Callable[[Any, ActorAddress], None]):
        """
        Subscribes to the specified message type.
        :param msg_type: Event type
        :param handler: Handler for the event
        :return:
        """
        if msg_type in self.handlers:
            logging.warning('Re-subscribe: %s', msg_type)
        self.handlers[msg_type] = handler

    def handle_delete_message(self):
        """
        Entity deletion message handler.
        :return:
        """
        logging.info(f'{self} got a message - ActorExitRequest')
        self.entity.is_deleting = True

    def receiveMessage(self, msg, sender):
        """
        Handles the received message. This method is called by the ActorSystem.
        :param msg:
        :param sender:
        :return:
        """
        logging.debug('%s received message: %s', self.name, msg)
        if isinstance(msg, ActorExitRequest):
            self.handle_delete_message()
            return

        if isinstance(msg, Message):

            message_type = msg.msg_type
            if message_type in self.handlers:
                try:
                    self.handlers[message_type](msg, sender)
                except Exception as ex:
                    traceback.print_exc()
                    logging.error(ex)
            else:
                logging.warning('%s There is no handler for message: %s', self.name, message_type)
            sender_name = self.dispatcher.reference_book.get_entity_name(sender)
            self_name = self.name
            ac_msg = (sender_name, self_name, message_type, msg.msg_body)
            self.scene.add_msg(ac_msg)
        else:
            logging.error('%s Wrong message format: %s', self.name, msg)
            super().receiveMessage(msg, sender)

    def __str__(self):
        return self.name

    def handle_init_message(self, message, sender):
        """
        Handles initialization message.
        :param message:
        :param sender:
        :return:
        """
        message_data = message.msg_body
        self.scene = message_data.get('scene')
        self.dispatcher = message_data.get('dispatcher')
        self.entity = message_data.get('entity')
        self.name = self.name + ' ' + self.entity.name
        logging.info(f'{self} initialized')
