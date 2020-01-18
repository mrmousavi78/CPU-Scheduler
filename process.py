from enums import State


class Process:
    def __init__(self, process_id, arrival_time, burst_time, io_time, state=State.NOT_ARRIVED):
        self.__process_id = process_id
        self.__arrival_time = arrival_time
        self.__next_arrival_time = arrival_time
        self.__burst_time = burst_time
        self.__io_time = io_time
        self.__stack = self.initialize()
        self.__state = state

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def minus_burst_time(self):
        self.__stack[len(self.__stack) - 1] -= 1
        if self.__stack[len(self.__stack) - 1] == 0:
            self.__stack.pop()
            if self.__stack:
                self.__state = State.IO
        self.check_terminate()

    def get_current_io_time(self):
        return self.__stack[len(self.__stack) - 1]

    def get_current_burst_time(self):
        return self.__stack[len(self.__stack) - 1]

    def get_next_arrival_time(self):
        return self.__next_arrival_time

    def set_next_arrival_time(self, time):
        self.__stack.pop()
        self.__next_arrival_time = time

    def check_terminate(self):
        if not self.__stack:
            self.__state = State.TERMINATED

    def initialize(self):
        stack = []

        if len(self.__burst_time) == len(self.__io_time):
            for i in range(len(self.__burst_time) - 1, -1, -1):
                stack.append(self.__io_time[i])
                stack.append(self.__burst_time[i])
        else:
            for i in range(len(self.__io_time) - 1, -1, -1):
                stack.append(self.__burst_time[i + 1])
                stack.append(self.__io_time[i])
            stack.append(self.__burst_time[0])

        return stack