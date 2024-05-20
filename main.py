from itertools import *
import time

def calc():
    for task in tasks.values():
        max_dep = max([tasks[i].end for i in task.deps], default=0)
        task.end = task.duration + max_dep + task.delay
        if task.end > max_len:
            return False
    return True


def build_timeline():
    timeline = [0] * max_len
    for i in tasks:
        for j in range(tasks[i].end - tasks[i].duration, tasks[i].end):
            timeline[j] += 1
    return timeline


def get_max_len(timeline, number_of_task):
    for i in range(len(timeline)):
        if timeline[i] != number_of_task:
            timeline[i] = ' '
    return max(map(len,''.join(map(str,timeline)).split()), default=0)

class Task:
    def __init__(self, duration, deps):
        self.deps = deps
        self.duration = duration
        self.delay = 0
        self.end = 0


tasks = {1: Task(3, []),
         2: Task(6, []),
         3: Task(7, [1, 2]),
         4: Task(10, [3]),
         5: Task(6, [3]),
         6: Task(8, [4, 5]),
         7: Task(7, [4]),
         8: Task(3, [6]),
         9: Task(1, [7, 8]),
         10: Task(4, []),
         11: Task(4, []),
         12: Task(2, [10]),
         13: Task(2, [12]),
         14: Task(11, [13]),
         15: Task(4, [8, 11])
}

number_of_tasks = 3

tasks = dict(sorted(tasks.items(), key=lambda x: max(x[1].deps, default=0)))

mx = 0
current = 0

max_len = 38


for N in range(5):
    for p in combinations(tasks, r=N):
        for task in tasks.values():
            task.delay = 0
        for comb in product(range(1, max_len), repeat=N):
            for task, delay in zip(p, comb):
                tasks[task].delay = delay
            if calc():
                current = get_max_len(build_timeline(), number_of_tasks)
                if current > mx:
                    mx = current
                    print(mx, {r: tasks[r].delay for r in p})

