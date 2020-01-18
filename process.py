from state import State


class Process:
    def __init__(self, process_id, arrival_time, burst_time, io_time, state=State.NOT_ARRIVED):
        self.__process_id = process_id
        self.__arrival_time = arrival_time
        self.__next_arrival_time = arrival_time
        self.__burst_time = burst_time
        self.__io_time = io_time
        self.__stack = self.initialize()
        self.__state = state

    def get_next_arrival_time(self, time):
        return self.__next_arrival_time

    def edit_arrival_time(self, next_arrival_time):
        self.__next_arrival_time = next_arrival_time

    def is_finished(self):
        if not self.__stack:
            self.__state = State.TERMINATED

    def initialize(self):
        stack = []
        if self.__burst_time.size() == self.__io_time.size():
            for i in range(self.__burst_time.size() - 1, -1, -1):
                stack.append(self.__io_time[i])
                stack.append(self.__burst_time[i])
        else:
            for i in range(self.__io_time.size() - 1, -1, -1):
                stack.append(self.__burst_time[i + 1])
                stack.append(self.__io_time[i])
            stack.append(self.__burst_time[0])

        return stack
