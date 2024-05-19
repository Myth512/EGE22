from itertools import *
import time
def calc():
    for i in tasks:
        tasks[i].end = tasks[i].time1 + max([tasks[e].end for e in tasks[i].deps], default=0) + tasks[i].delay
    return max([task.end for task in tasks.values()])


def build_timeline():
    timeline = [0] * max_len
    for i in tasks:
        for j in range(tasks[i].end - tasks[i].time1, tasks[i].end):
            timeline[j] += 1
    return timeline


def get_max_len(timeline, number_of_task):
    for i in range(len(timeline)):
        if timeline[i] != number_of_task:
            timeline[i] = ' '
    return max(map(len, ''.join(map(str, timeline)).split()), default=0)

class Task:
    def __init__(self, time1, deps):
        self.deps = deps
        self.time = time1
        self.delay = 0
        self.end = None


tasks = {1: Task(2, []),
         2: Task(5, [1]),
         3: Task(6, [1]),
         4: Task(3, [2, 3]),
         5: Task(8, [4]),
         6: Task(5, [4]),
         7: Task(2, [6]),
         8: Task(3, [5, 7]),
         9: Task(7, []),
         10: Task(6, [9]),
         11: Task(4, [9]),
         12: Task(5, []),
         13: Task(9, [12])}

number_of_tasks = 3

tasks = dict(sorted(tasks.items(), key=lambda x: max(x[1].deps, default=0))) # тут есть баг

mx = 0
current = 0
max_len = calc()
N = 3
# 210

start = time.time()

for pr in permutations(tasks, r=N):
    for i in tasks:
        tasks[i].delay = 0
    all_combinations = product(range(max_len), repeat=N)
    for comb in all_combinations:
        delays = dict(zip(pr, comb))
        for i in pr:
            tasks[i].delay = delays[i]
        if calc() <= max_len:
            current = get_max_len(build_timeline(), number_of_tasks)
            if current > mx:
                mx = current
                print(mx, delays)

print(time.time() - start)