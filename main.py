from scheduler import Scheduler
from process import Process
from enums import Algorithm
import copy
import threading
import csv


def csv_parser(file_path):
    processes = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        read_on = False
        for row in csv_reader:
            if read_on:
                processes.append(Process(int(row[0]), int(row[1]), [int(x) for x in row[2][1:-1].split(', ')], [int(x) for x in row[3][1:-1].split(', ')]))
            read_on = True
    return processes


def main():
    file_path = "/Users/VahidGh/Documents/Operating System/CPU-Scheduler/processes.csv"
    processes = csv_parser(file_path=file_path)
    processes_fcfs = copy.deepcopy(processes)
    processes_rr = copy.deepcopy(processes)
    processes_spn = copy.deepcopy(processes)
    processes_srt = copy.deepcopy(processes)
    scheduler_fcfs = Scheduler()
    scheduler_rr = Scheduler()
    scheduler_spn = Scheduler()
    scheduler_srt = Scheduler()
    scheduler_fcfs.processes = processes_fcfs
    scheduler_rr.processes = processes_rr
    scheduler_spn.processes = processes_spn
    scheduler_srt.processes = processes_srt
    th_fcfs = threading.Thread(target=scheduler_fcfs.run(algorithm=Algorithm.FCFS))
    th_rr = threading.Thread(target=scheduler_rr.run(algorithm=Algorithm.RR))
    th_spn = threading.Thread(target=scheduler_spn.run(algorithm=Algorithm.SPN))
    th_srt = threading.Thread(target=scheduler_srt.run(algorithm=Algorithm.SRT))
    th_fcfs.start()
    th_rr.start()
    th_spn.start()
    th_srt.start()
    th_fcfs.join()
    th_rr.join()
    th_spn.join()
    th_srt.join()
    print('scheduling finished :)')


if __name__ == '__main__':
    main()
