from enum import Enum


class State(Enum):
    NOT_ARRIVED = 0
    READY = 1
    CPU = 2
    IO = 3
    IOTER = 4
    TERMINATED = 5


class Algorithm(Enum):
    FCFS = 0
    RR = 1
    SPN = 2
    SRT = 3
