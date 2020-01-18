class Scheduler:
    """
    A machine that simulate the execution of processes in different algorithms. :)
    """

    def __init__(self):
        self.__state = None
        self.__current_algorithm = None
        self.__processes = []
        self.__running_process = 0
        self.__ready_queue = []  # TODO: find a implementation for queue
        self.__done_list = []
        self.__timer = 0

    def get_processes(self, processes):
        self.__processes = processes


    def FCFS(self):
        pass


    def run(self):
        pass
