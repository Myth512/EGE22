from itertools import *

def calc():
    '''функция производит вычисления положения процессов на таймлайне'''
    for task in tasks:
        max_dep = max([tasks[i-1].end for i in task.deps], default=0)
        task.end = task.duration + max_dep + task.delay
        if task.end > threshold:
            return False
    return True


def build_timeline():
    '''функция строит таймлайн в ввиде массива чисел,
     отражающих кол-во процеесов в момент времени'''
    timeline = [0] * threshold
    for task in tasks:
        for i in range(task.end - task.duration, task.end):
            timeline[i] += 1
    return timeline


def get_max_len(timeline, number):
    '''функция возвращает длину максимального отрезка, состоящего только из числа number'''
    for i in range(len(timeline)):
        if timeline[i] != number:
            timeline[i] = ' '
    return max(map(len, ''.join(map(str, timeline)).split()), default=0)

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

target_number_of_tasks = 3

# порядок в котором надо обрабатывать процессы
order = [tasks.index(i) for i in sorted(tasks, key=lambda x: max(x.deps, default=0))]

# сейчас это магическое число, но я потом пофикшу
threshold = 24 # максимальная длина таймлайна

max_length = 0
current_length = 0

for number_of_tasks in range(5):
    for task_combinations in combinations(order, r=number_of_tasks):
        for task in tasks:
            task.delay = 0
        for delay_combinations in product(range(1, threshold), repeat=number_of_tasks):
            for task, delay in zip(task_combinations, delay_combinations):
                tasks[task].delay = delay
            if calc():
                current_length = get_max_len(build_timeline(), target_number_of_tasks)
                if current_length > max_length:
                    max_length = current_length
                    print(max_length, {i+1: tasks[i].delay for i in task_combinations})
