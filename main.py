from itertools import *

def calc():
    for task in tasks:
        max_dep = max([tasks[i-1].end for i in task.deps], default=0)
        task.end = task.duration + max_dep + task.delay
        if task.end > max_len:
            return False
    return True


def build_timeline():
    timeline = [0] * max_len
    for task in tasks:
        for i in range(task.end - task.duration, task.end):
            timeline[i] += 1
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
        self.end = None


tasks = [Task(2, []),
         Task(5, [1]),
         Task(6, [1]),
         Task(3, [2, 3]),
         Task(8, [4]),
         Task(5, [4]),
         Task(2, [6]),
         Task(3, [5, 7]),
         Task(7, []),
         Task(6, [9]),
         Task(4, [9]),
         Task(5, []),
         Task(9, [12])]

number_of_tasks = 3

# порядок в котором надо обрабатывать процессы
order = [tasks.index(i) for i in sorted(tasks, key=lambda x: max(x.deps, default=0))]

max_len = 24

mx = 0
current = 0

for N in range(5):
    for task_combinations in combinations(order, r=N):
        for task in tasks:
            task.delay = 0
        for delay_combinations in product(range(1, max_len), repeat=N):
            for task, delay in zip(task_combinations, delay_combinations):
                tasks[task].delay = delay
            if calc():
                current = get_max_len(build_timeline(), number_of_tasks)
                if current > mx:
                    mx = current
                    print(mx, {r+1: tasks[r].delay for r in task_combinations})
