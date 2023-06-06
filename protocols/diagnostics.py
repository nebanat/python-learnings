from protocols.device import Device

def collect_diagnostics(device: Device) -> None:
    print("Connecting to diagnostics server .")
    status = device.status_update()
    print(f"sending status update [{status}] to server")