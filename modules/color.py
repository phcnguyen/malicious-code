# IMPORT MODULES
from os import execv, system as _system, name as _os_name
from sys import executable, argv
from collections import deque

class Colors:
    @staticmethod
    def make_ansi(col: str, text: str) -> str:
        return f"\033[38;2;{col}m{text}\033[38;2;255;255;255m"
    
    @staticmethod
    def remove_ansi(col: str) -> str:
        return col.replace('\033[38;2;', '').replace('m','').replace('50m', '').replace('\x1b[38', '')
    
    @staticmethod
    def start(color: str) -> str:
        return f"\033[38;2;{color}m"
    
    @staticmethod
    def get_spaces(text: str) -> int:
        return len(text) - len(text.lstrip())
    
    @staticmethod
    def mix_colors(col1: str, col2: str) -> list:
        col1, col2 = Colors.remove_ansi(col=col1), Colors.remove_ansi(col=col2)
        return deque([col1, col2]) if col1 == col2 else deque([col1, Colors.static_mix([col1, col2], _start=False), col2])

class Color:
    @staticmethod
    def static_mix(colors: list, _start: bool = True) -> str:
        rgb = [list(map(int, Colors.remove_ansi(col).split(';'))) for col in colors]
        average_rgb = [round(sum(color[i] for color in rgb) / len(rgb)) for i in range(3)]
        rgb_string = ';'.join(map(str, average_rgb))
        return Colors.start(rgb_string) if _start else rgb_string
    
class System:
    def __init__(self):
        self.Windows = _os_name == 'nt'

    def init(self):
        _system('')

    def clear(self):
        return _system("cls" if self.Windows else "clear")

    def title(self, title: str):
        if self.Windows:
            return _system(f"title {title}")

    def size(self, x: int, y: int):
        if self.Windows:
            return _system(f"mode {x}, {y}")
    
    def reset(self):
        execv(executable, [executable] + argv)   

class Col:
    Red = Colors.start('255;0;0')
    
    Blue = Colors.start('28;121;255')
    Cyan = Colors.start('0;255;255')
    Pink = Colors.start('255,192,203')

    Black = Colors.start('0;0;0')
    White = Colors.start('255;255;255')
    Green = Colors.start('0;255;0')

    Purple = Colors.start('255;0;255')
    Yellow = Colors.start('255;255;0')
    Orange = Colors.start('255;165;0')