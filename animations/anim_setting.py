from animations.animation_tape import AnimationTape


class AnimationSetting:
    def __init__(self, tape: AnimationTape, repeat_time: int) -> None:
        self._tape = tape
        self._repeat_time = repeat_time

    @property
    def tape(self) -> AnimationTape:
        return self._tape

    @property
    def repeat_time(self) -> int:
        return self._repeat_time
