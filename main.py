from scheduler import Scheduler
from process import Process
from enums import Algorithm

processes = []
for i in range(3):
    processes.append(Process(i + 1, i, [10], [2]))

scheduler_fcfs = Scheduler()
scheduler_rr = Scheduler()
scheduler_spn = Scheduler()
scheduler_srt = Scheduler()
scheduler_fcfs.processes = processes
scheduler_rr.processes = processes
scheduler_spn.processes = processes
scheduler_srt.processes = processes
scheduler_fcfs.run(Algorithm.FCFS)
scheduler_rr.run(Algorithm.RR)
scheduler_spn.run(Algorithm.SPN)
scheduler_srt.run(Algorithm.SRT)
scheduler_fcfs.detail()
scheduler_rr.detail()
scheduler_spn.detail()
scheduler_srt.detail()
print('scheduling finished :)')
