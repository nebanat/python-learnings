from abc import ABC, abstractmethod
from iot.message import MessageType

class Device(ABC):
    """
    Abstarct base class that defines the interface for devices
    """
    @abstractmethod
    def connect(self) -> None:
        """connect abstract base class"""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """disconnect abstract base class"""
        pass

    @abstractmethod
    def send_message(self, message_type: MessageType, data:str) -> None:
        """
        send message abstract method 

        Args:
            message_type (MessageType): Message Type Enum e.g. SWITCH_ON, SWITCH_OFF
            data (str): message data 
        """
        pass

    @abstractmethod
    def status_update(self) -> str:
        """
        status update abstract method

        Returns:
            str: status message
        """
        pass
