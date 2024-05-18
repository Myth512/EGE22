from itertools import *

def calc():
    for i in tasks:
        tasks[i].end = tasks[i].time + max([tasks[e].end for e in tasks[i].deps]) + tasks[i].delay
        if tasks[i].end > 38:
            return False
    return True


def show_timeline():
    timeline = [0] * 38
    for i in tasks:
        for j in range(tasks[i].end - tasks[i].time, tasks[i].end):
            timeline[j] += 1
    return timeline


class Task:
    def __init__(self, time, deps, ranges=range(1), delay=0, end=0):
        self.deps = deps
        self.time = time
        self.ranges = ranges
        self.delay = 0
        self.end = 0


tasks = {0: Task(0, [0]),
         1: Task(5, [0], range(5)),
         2: Task(4, [0], range(5)),
         3: Task(8, [1, 2], range(2)),
         4: Task(7, [3], range(2)),
         5: Task(8, [3], range(2)),
         6: Task(4, [4], range(2)),
         7: Task(3, [5, 6], range(2)),
         8: Task(1, [7], range(2)),
         9: Task(9, [0], range(10, 15)),
         10: Task(8, [0], range(10, 15)),
         11: Task(7, [0], range(10, 15)),
         12: Task(6, [10], range(2)),
         13: Task(5, [10, 11], range(2))
}

tasks = dict(sorted(tasks.items(), key=lambda x: max(x[1].deps)))

mx = 0
current = 0

range_values = [i.ranges for i in tasks.values()]
all_combinations = product(*range_values)

for comb in all_combinations:
    delays = dict(zip(tasks, comb))
    for i in tasks:
        tasks[i].delay = delays[i]
    if calc():
        current = show_timeline().count(5)
        if current > mx:
            mx = current
            print(mx, delays, show_timeline(), "\n")
