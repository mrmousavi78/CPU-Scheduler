from state import State


class Process:
    def __init__(self, process_id, arrival_time, burst_time, io_time, state=State.NOT_ARRIVED):
        self.__process_id = process_id
        self.__arrival_time = arrival_time
        self.__burst_time = burst_time
        self.__io_time = io_time
        self.__state = state


