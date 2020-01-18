from enum import Enum


class State(Enum):
    NOT_ARRIVED = 0
    READY = 1
    CPU = 2
    IO = 3
    TERMINATED = 4
