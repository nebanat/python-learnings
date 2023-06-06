import string
import random
from typing import Protocol
# from protocols.device import Device
from protocols.message import Message, MessageType

def generate_id(length: int = 8):
    return "".join(random.choices(string.ascii_uppercase, k=length))


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


class IOTService:
    """
    IOTService that manages the device interations such as:
        - Registering a device 
        - Unregistering a device
        - retrieving device details
        - run programs on devices
    """
    def __init__(self) -> None:
        """
        initialization method with all devices
        """
        self.devices: dict[str, Device] = {}
    
    def register_device(self, device: Device) -> str:
        """
        register a device 

        Args:
            device (Device): Device instance

        Returns:
            str: device id
        """
        # connnect to device
        device.connect()
        # generate a device id 
        device_id = generate_id()
        # create a dict mapping to device
        self.devices[device_id] = device
        return device_id
    
    def unregister_device(self, device_id: str) -> None:
        """
        Unregister a device 

        Args:
            device_id (str): device id
        """
        # disconnect to device if it is connected 
        self.devices[device_id].disconnect()
        # remove from device mappings
        del self.devices[device_id]
    
    def get_device(self, device_id: str) -> Device:
        """
        get an instance of a device

        Args:
            device_id (str): device id

        Returns:
            Device: Device instance
        """
        return self.devices[device_id]
    
    def run_program(self, program: list[Message]) -> None:
        print("===== Running Program ====")
        for msg in program:
            self.devices[msg.device_id].send_message(msg.msg_type, msg.data)
        print("=====END OF PROGRAM")