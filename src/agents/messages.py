from enum import Enum
from dataclasses import dataclass
from typing import Any


class MessageType(Enum):
    INIT_MESSAGE = 'Initialization'
    NEW_TIME_MESSAGE = 'New time'


@dataclass
class Message:
    """
    A message to be sent to the other agents.
    """
    msg_type: MessageType
    msg_body: Any
