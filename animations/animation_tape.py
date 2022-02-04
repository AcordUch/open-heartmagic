class AnimationTape:
    def __init__(
            self, start_frames: list[str] = None,
            loop_frames: list[str] = None,
            end_frames: list[str] = None
    ) -> None:
        self._start_frames: list[str] = (list() if start_frames is None
                                         else start_frames)
        self._loop_frames: list[str] = (list() if loop_frames is None
                                        else loop_frames)
        self._end_frames: list[str] = (list() if end_frames is None
                                       else end_frames)

    def get_start_frames(self) -> list[str]:
        return self._start_frames

    def get_loop_frames(self) -> list[str]:
        return self._loop_frames

    def get_end_frames(self) -> list[str]:
        return self._end_frames

