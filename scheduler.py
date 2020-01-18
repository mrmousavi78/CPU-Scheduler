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
        self.__ready_queue = []  # TODO: find a implementation for queue
        self.__done_list = []
        self.__timer = 0

    def get_processes(self, processes):
        self.__processes = processes

    def update_ready_queue(self):
        for proc in self.__processes:
            if proc.get_next_arrival_time() == self.__timer:
                self.__ready_queue.append(proc)
        if self.__algorithm == Algorithm.SPN or self.__algorithm == Algorithm.SRT:
            self.__ready_queue.sort(key=lambda x: x.get_current_burst_time())

    def FCFS(self):
        while len(self.__done_list) != len(self.__processes):
            if self.__ready_queue:
                self.update_ready_queue()
                self.__running_process = self.__ready_queue.pop(0)
                self.__running_process.minus_burst_time()


        pass

    def run(self):
        pass
