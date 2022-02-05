from random import choice
from typing import Callable


class BlinkingHeart:
    _HEART: str = '🤍️'
    _COLORED_HEARTS: list[str] = ['💚', '💙', '💜', '❤', '💛', '🧡']

    _MAP: str = '''
0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 1 0 0
0 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0
'''

    def __init__(self, number_of_blinks: int = 10) -> None:
        self._number_of_blinks = number_of_blinks

    def _generate_by_mask(self) -> str:
        def _choice() -> str:
            return choice(self._COLORED_HEARTS)

        _CONVERTER: dict[str: Callable[[], str]] = {
            '\n': lambda: '\n',
            '0': lambda: self._HEART,
            '1': _choice
        }

        output = ''
        for char in self._MAP:
            output += (
                _CONVERTER[char]() if _CONVERTER.get(char) is not None
                else char
            )
        return output

    def generate_tape(self) -> list[str]:
        return [
            self._generate_by_mask() for _ in range(self._number_of_blinks)
        ]
