from protocols.devices import Curtains, HueLight, SmartSpeaker
from protocols.diagnostics import collect_diagnostics
from protocols.message import Message, MessageType
from protocols.service import IOTService

def main() -> None:
    service = IOTService()

    hue_light = HueLight()
    speaker = SmartSpeaker()
    curtains = Curtains()
    
    hue_light_id = service.register_device(hue_light)
    speaker_id = service.register_device(speaker)
    curtains_id = service.register_device(curtains)

    wake_up_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, "Miles Davis - Kind of Blue"),
        Message(curtains_id, MessageType.OPEN)
    ]

    sleep_program = [
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
        Message(curtains_id, MessageType.CLOSE)
    ]

    service.run_program(wake_up_program)
    service.run_program(sleep_program)

    collect_diagnostics(hue_light)