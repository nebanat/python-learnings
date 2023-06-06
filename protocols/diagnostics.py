# from protocols.device import Device
from typing import Protocol

class DiagnosticSource(Protocol):
    """
    Abstarct base class that defines the interface for devices
    """

    def status_update(self) -> str:
        """
        status update abstract method

        Returns:
            str: status message
        """
        ...


def collect_diagnostics(source: DiagnosticSource) -> None:
    print("Connecting to diagnostics server .")
    status = source.status_update()
    print(f"sending status update [{status}] to server")