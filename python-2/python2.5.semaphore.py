from enum import Enum


class Colors(Enum):
    red = 'red'
    orange = 'orange'
    green = 'green'
    orangered = 'orangered'


class Semaphore:
    sequence = [
        Colors.red,
        Colors.orangered,
        Colors.green,
        Colors.orange
    ]

    def __init__(self):
        self.current_index = 0

    def change_state(self):
        self.current_index += 1

    def get_status(self):
        return self.sequence[self.current_index]

    def set_status(self, status):
        index = self.sequence.index(status)
        self.current_index = index