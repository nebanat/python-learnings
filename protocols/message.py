from dataclasses import dataclass
from enum import Enum, auto

class MessageType(Enum):
    SWITCH_OFF = auto()
    SWITCH_ON = auto()
    CHANGE_COLOR = auto()
    PLAY_SONG = auto()
    OPEN = auto()
    CLOSE = auto()

@dataclass
class Message:
    device_id: str
    msg_type: MessageType
    data: str = ""
