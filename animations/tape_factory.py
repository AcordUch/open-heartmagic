from .animation_tape import AnimationTape
from . import templates


class TapeFactory:
    @staticmethod
    def get_example() -> AnimationTape:
        return AnimationTape(
            templates.Example.START,
            templates.Example.LOOP,
            templates.Example.END
        )

    @staticmethod
    def get_pulse_heart() -> AnimationTape:
        return AnimationTape(
            templates.PulseHeart.START,
            templates.PulseHeart.LOOP,
            templates.PulseHeart.END
        )

    @staticmethod
    def get_increasing() -> AnimationTape:
        return AnimationTape(
            templates.PulseHeart.START
        )
