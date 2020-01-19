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

    def average_response_time(self):
        art = 0
        for process in self.__processes:
            art += process.response_time
        return art

    def average_waiting_time(self):
        awt = 0
        for process in self.__processes:
            awt += process.waiting_time
        return awt

    def average_turn_around_time(self):
        att = 0
        for process in self.__processes:
            att += process.turn_around_time
        return att

    @property
    def processes(self):
        return self.__processes

    @processes.setter
    def processes(self, procs):
        self.__processes = procs

    def update_ready_queue(self):
        for proc in self.__processes:
            if proc.next_arrival_time == self.__timer and proc.state != State.IO_TERMINATED:
                if proc.state == State.IO:
                    proc.state = State.READY
                self.__ready_queue.append(proc)
            if proc.next_arrival_time == self.__timer and proc.state == State.IO_TERMINATED:
                proc.state = State.TERMINATED
                proc.turn_around_time = self.__timer - proc.arrival_time
                self.__done_list.append(proc)
        if self.__algorithm == Algorithm.SPN or self.__algorithm == Algorithm.SRT:
            self.__ready_queue.sort(key=lambda x: x.burst_time)

    def FCFS(self):
        self.update_ready_queue()
        while len(self.__done_list) != len(self.__processes):
            if self.__ready_queue:
                self.__running_process = self.__ready_queue.pop(0)
                self.__running_process.state = State.CPU
                if self.__running_process.response_time == -1:
                    self.__running_process.response_time = self.__timer - self.__running_process.arrival_time
                while self.__running_process.state == State.CPU:
                    self.__running_process.minus_burst_time()
                    if self.__running_process.state == State.IO:
                        self.__running_process.next_arrival_time = self.__timer + self.__running_process.io_time + 1
                    elif self.__running_process.state == State.TERMINATED:
                        self.__running_process.turn_around_time = self.__timer - self.__running_process.arrival_time
                        self.__done_list.append(self.__running_process)
                    self.__timer += 1
                    self.increment_waiting_time()
                    self.update_ready_queue()
            else:
                self.__timer += 1
                self.update_ready_queue()

    def RR(self):
        self.update_ready_queue()
        while len(self.__done_list) != len(self.__processes):
            if self.__ready_queue:
                self.__running_process = self.__ready_queue.pop(0)
                self.__running_process.state = State.CPU
                if self.__running_process.response_time == -1:
                    self.__running_process.response_time = self.__timer - self.__running_process.arrival_time
                counter = 0
                while self.__running_process.state == State.CPU:
                    self.__running_process.minus_burst_time()
                    if self.__running_process.state == State.IO:
                        self.__running_process.next_arrival_time = self.__timer + self.__running_process.io_time + 1
                    elif self.__running_process.state == State.TERMINATED:
                        self.__running_process.turn_around_time = self.__timer - self.__running_process.arrival_time
                        self.__done_list.append(self.__running_process)
                    counter += 1
                    self.__timer += 1
                    self.increment_waiting_time()
                    if counter == 5 and (self.__running_process.state not in [State.IO, State.IO_TERMINATED, State.TERMINATED]):
                        self.__running_process.state = State.READY
                        self.__running_process.next_arrival_time = self.__timer
                    self.update_ready_queue()
            else:
                self.__timer += 1
                self.update_ready_queue()

    def SPN(self):
        self.update_ready_queue()
        while len(self.__done_list) != len(self.__processes):
            if self.__ready_queue:
                self.__running_process = self.__ready_queue.pop(0)
                self.__running_process.state = State.CPU
                if self.__running_process.response_time == -1:
                    self.__running_process.response_time = self.__timer - self.__running_process.arrival_time
                while self.__running_process.state == State.CPU:
                    self.__running_process.minus_burst_time()
                    if self.__running_process.state == State.IO:
                        self.__running_process.next_arrival_time = self.__timer + self.__running_process.io_time + 1
                    elif self.__running_process.state == State.TERMINATED:
                        self.__running_process.turn_around_time = self.__timer - self.__running_process.arrival_time
                        self.__done_list.append(self.__running_process)
                    self.__timer += 1
                    self.increment_waiting_time()
                    self.update_ready_queue()
            else:
                self.__timer += 1
                self.update_ready_queue()

    def SRT(self):
        self.update_ready_queue()
        while len(self.__done_list) != len(self.__processes):
            if self.__ready_queue:
                self.__running_process = self.__ready_queue.pop(0)
                self.__running_process.state = State.CPU
                if self.__running_process.response_time == -1:
                    self.__running_process.response_time = self.__timer - self.__running_process.arrival_time
                while self.__running_process.state == State.CPU:
                    self.__running_process.minus_burst_time()
                    if self.__running_process.state == State.IO:
                        self.__running_process.next_arrival_time = self.__timer + self.__running_process.io_time + 1
                    elif self.__running_process.state == State.TERMINATED:
                        self.__running_process.turn_around_time = self.__timer - self.__running_process.arrival_time
                        self.__done_list.append(self.__running_process)
                    self.__timer += 1
                    self.increment_waiting_time()
                    self.update_ready_queue()
                    if self.__running_process.burst_time > self.__ready_queue[0].burst_time:
                        self.__running_process.state = State.READY
                        self.__running_process.next_arrival_time = self.__timer
                        self.update_ready_queue()
                        break
            else:
                self.__timer += 1
                self.update_ready_queue()

    def increment_waiting_time(self):
        for proc in self.__processes:
            if proc.state == State.READY:
                proc.waiting_time += 1

    def run(self, algorithm):
        self.__algorithm = algorithm
        if self.__algorithm == Algorithm.FCFS:
            self.FCFS()
        elif self.__algorithm == Algorithm.RR:
            self.RR()
