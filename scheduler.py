from enums import Algorithm, State


class Scheduler:
    """
    A machine that simulate the execution of processes in different algorithms. :)
    """

    def __init__(self):
        self.__state = None
        self.__algorithm = None
        self.__processes = []
        self.__running_process = None
        self.__ready_queue = []
        self.__done_list = []
        self.__timer = 0

    def set_processes(self, processes):
        self.__processes = processes

    def update_ready_queue(self):
        for proc in self.__processes:
            if proc.get_next_arrival_time() == self.__timer:
                if proc.get_state() == State.IO:
                    proc.set_state(State.READY)
                self.__ready_queue.append(proc)
        if self.__algorithm == Algorithm.SPN or self.__algorithm == Algorithm.SRT:
            self.__ready_queue.sort(key=lambda x: x.get_current_burst_time())

    def FCFS(self):
        self.update_ready_queue()
        while len(self.__done_list) != len(self.__processes):
            if self.__ready_queue:
                self.__running_process = self.__ready_queue.pop(0)
                self.__running_process.set_state(State.CPU)
                while self.__running_process.get_state() == State.CPU:
                    self.__running_process.minus_burst_time()
                    if self.__running_process.get_state() == State.IO:
                        self.__running_process.set_next_arrival_time(self.__timer + self.__running_process.get_current_io_time() + 1)
                    elif self.__running_process.get_state() == State.TERMINATED:
                        self.__done_list.append(self.__running_process)
                    self.__timer += 1
                    self.update_ready_queue()

    def RR(self):
        self.update_ready_queue()
        while len(self.__done_list) != len(self.__processes):
            if self.__ready_queue:
                self.__running_process = self.__ready_queue.pop(0)
                self.__running_process.set_state(State.CPU)
                counter = 0
                while self.__running_process.get_state() == State.CPU:
                    self.__running_process.minus_burst_time()
                    if self.__running_process.get_state() == State.IO:
                        self.__running_process.set_next_arrival_time(self.__timer + self.__running_process.get_current_io_time() + 1)
                    elif self.__running_process.get_state() == State.TERMINATED:
                        self.__done_list.append(self.__running_process)  # TODO: fix the last process io bug
                    counter += 1
                    self.__timer += 1
                    if counter == 5:
                        self.__running_process.set_state(State.READY)
                        self.__running_process.set_next_arrival_time(self.__timer)
                    self.update_ready_queue()
            else:
                self.__timer += 1
                self.update_ready_queue()

    def run(self, algorithm):
        self.__algorithm = algorithm
        if self.__algorithm == Algorithm.FCFS:
            self.FCFS()
        elif self.__algorithm == Algorithm.RR:
            self.RR()
