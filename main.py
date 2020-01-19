from scheduler import Scheduler
from process import Process
from enums import Algorithm
import copy

processes = []
for i in range(3):
    processes.append(Process(i + 1, i, [12, 6], [8]))

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
scheduler_fcfs.run(Algorithm.FCFS)
scheduler_rr.run(Algorithm.RR)
scheduler_spn.run(Algorithm.SPN)
scheduler_srt.run(Algorithm.SRT)
scheduler_fcfs.detail()
scheduler_rr.detail()
scheduler_spn.detail()
scheduler_srt.detail()
print('scheduling finished :)')
