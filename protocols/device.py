from typing import Protocol
from protocols.message import MessageType

class Device(Protocol):
    """
    Abstarct base class that defines the interface for devices
    """
    def connect(self) -> None:
        """connect protocol base method"""
        ...

    def disconnect(self) -> None:
        """disconnect protocol base method"""
        ...

    def send_message(self, message_type: MessageType, data:str) -> None:
        """
        send message abstract method 

        Args:
            message_type (MessageType): Message Type Enum e.g. SWITCH_ON, SWITCH_OFF
            data (str): message data 
        """
        ...

    def status_update(self) -> str:
        """
        status update abstract method

        Returns:
            str: status message
        """
        ...
