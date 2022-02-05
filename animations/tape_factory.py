from .animation_tape import AnimationTape
from . import templates
from .blinking_heart import BlinkingHeart


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

    @staticmethod
    def get_blinking_heart(number_of_blinks: int = 10) -> AnimationTape:
        return AnimationTape(
            templates.PulseHeart.START,
            BlinkingHeart(number_of_blinks).generate_tape(),
            templates.Smooth.END
        )
