from animations.animation_tape import AnimationTape


class AnimationSetting:
    def __init__(self, control: AnimationTape, repeat_time: int) -> None:
        self._control = control
        self._repeat_time = repeat_time

    @property
    def control(self) -> AnimationTape:
        return self._control

    @property
    def repeat_time(self) -> int:
        return self._repeat_time
