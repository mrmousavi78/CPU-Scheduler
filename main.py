from scheduler import Scheduler
from process import Process
from enums import Algorithm

processes = []
for i in range(3):
    processes.append(Process(i + 1, i, [6, 2], [8]))

scheduler = Scheduler()
scheduler.processes = processes
scheduler.run(Algorithm.SPN)
print(scheduler.average_response_time())
print(scheduler.average_turn_around_time())
print(scheduler.average_waiting_time())
print(scheduler.cpu_utilization())
print('scheduling finished :)')
