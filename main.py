from scheduler import Scheduler
from process import Process
from enums import Algorithm

processes = []
for i in range(3):
    processes.append(Process(i, i, [6, 2], [1]))

scheduler = Scheduler()
scheduler.set_processes(processes)
scheduler.run(Algorithm.RR)
print('Hello')