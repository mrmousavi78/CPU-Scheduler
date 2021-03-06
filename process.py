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
        self.__response_time = -1
        self.__turn_around_time = -1
        self.__waiting_time = 0
        self.__terminate_time = 0

    @property
    def terminate_time(self):
        return self.__terminate_time

    @terminate_time.setter
    def terminate_time(self, t_time):
        self.__terminate_time = t_time

    @property
    def process_id(self):
        return self.__process_id

    @property
    def turn_around_time(self):
        return self.__turn_around_time

    @turn_around_time.setter
    def turn_around_time(self, t_time):
        self.__turn_around_time = t_time

    @property
    def waiting_time(self):
        return self.__waiting_time

    @waiting_time.setter
    def waiting_time(self, w_time):
        self.__waiting_time = w_time

    @property
    def response_time(self):
        return self.__response_time

    @response_time.setter
    def response_time(self, r_time):
        self.__response_time = r_time

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        self.__state = new_state

    def minus_burst_time(self):
        self.check_terminate()
        if self.__state != State.TERMINATED:
            self.__stack[-1] -= 1
            if self.__stack[-1] == 0:
                self.__stack.pop()
                if self.__stack:
                    self.__state = State.IO
            self.check_terminate()

    @property
    def arrival_time(self):
        return self.__arrival_time

    @property
    def io_time(self):
        return self.__stack[-1]

    @property
    def burst_time(self):
        if self.__stack:
            return self.__stack[-1]
        else:                               # this condition must be check
            return 0

    @property
    def next_arrival_time(self):
        return self.__next_arrival_time

    @next_arrival_time.setter
    def next_arrival_time(self, time):
        if self.__state == State.IO:
            self.__stack.pop()
        self.__next_arrival_time = time
        if not self.__stack:
            self.__state = State.IO_TERMINATED

    def increment_waiting_time(self):
        self.__waiting_time += 1

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
