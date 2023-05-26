from iot.message import MessageType
from iot.device import Device
from iot.message import MessageType

class HueLight(Device):
    """
    Hue light device inherits from device ABC 
    """
    def connect(self) -> None:
        """
        Hue light connect implementation 
        """
        print("Connecting Hue Light")
    
    def disconnect(self) -> None:
        """
        Hue light disconnect implementation
        """
        print("Disconnecting Hue light")
    
    def send_message(self, message_type: MessageType, data: str) -> None:
        """
        Hue light implementation of send message

        Args:
            message_type (MessageType): message type 
            data (str): message data 
        """
        print(
            f"Hue light handling message of type {message_type.name} with data [{data}]"
        )
    
    def status_update(self) -> str:
        """
        Hue status update method

        Returns:
            str: status update message 
        """
        return "hue_light_status_ok"


class SmartSpeaker(Device):
    def connect(self) -> None:
        """
        Smart speaker connect implementation
        """
        print("Connecting Smart Speaker")
    
    def disconnect(self) -> None:
        """
        Smart speaker disconnect implementation
        """
        print("Disconnecting Smart Speaker")
    
    def send_message(self, message_type: MessageType, data: str) -> None:
        """
       Smart speaker implementation of send message

        Args:
            message_type (MessageType): message type 
            data (str): message data 
        """
        print(
            f"Smart Speaker handling message of type {message_type.name} with data [{data}]"
        )
    
    def status_update(self) -> str:
        """
        Smart speaker update method

        Returns:
            str: status update message 
        """
        return "smart_speaker_status_ok"

class Curtains(Device):
    def connect(self) -> None:
        """
        Curtains connect implementation
        """
        print("Connecting Curtains")
    
    def disconnect(self) -> None:
        """
        Curtains disconnect implementation
        """
        print("Disconnecting Curtains")
    
    def send_message(self, message_type: MessageType, data: str) -> None:
        """
        Curtains implementation of send message

        Args:
            message_type (MessageType): message type 
            data (str): message data 
        """
        print(
            f"Curtains handling message of type {message_type.name} with data [{data}]"
        )
    
    def status_update(self) -> str:
        """
        Curtains status update method

        Returns:
            str: status update message 
        """
        return "curtains_status_ok"
