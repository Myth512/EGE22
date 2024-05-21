from itertools import *

def calc():
    '''функция производит вычисления положения процессов на таймлайне'''
    for i in order:
        max_dep = max([tasks[e-1].end for e in tasks[i].deps], default=0)
        tasks[i].end = tasks[i].delay + max_dep + tasks[i].duration
        if tasks[i].end > threshold:
            return False
    return True


def timeline():
    '''функция строит таймлайн в ввиде массива чисел,
     отражающих кол-во исполняемых процеcсов в момент времени'''
    timeline = [0] * threshold
    for task in tasks:
        for i in range(task.end - task.duration, task.end):
            timeline[i] += 1
    return timeline


def max_section(timeline, number):
    '''функция возвращает длину максимального отрезка, состоящего только из числа number'''
    for i in range(threshold):
        if timeline[i] != number:
            timeline[i] = ' '
    return max(map(len, ''.join(map(str, timeline)).split()), default=0)


class Task:
    def __init__(self, duration, deps):
        self.deps = deps
        self.duration = duration
        self.delay = 0
        self.end = None


tasks = [Task(10, []),
         Task(12, []),
         Task(6, [1, 2]),
         Task(12, [3]),
         Task(16, [3]),
         Task(10, [3]),
         Task(9, []),
         Task(9, []),
         Task(7, [7, 8]),
         Task(3, [9]),
         Task(8, []),
         Task(8, [11])]


# количество процессов из условия
target_number_of_tasks = 6

# порядок в котором надо обрабатывать процессы
order = [tasks.index(i) for i in sorted(tasks, key=lambda x: max(x.deps, default=0))]

# сейчас это магическое число, но я потом пофикшу
threshold = 37 # максимальная длина таймлайна

max_length = 0
current_length = 0

for number_of_tasks in range(5):
    for task_combinations in combinations(order, r=number_of_tasks):
        for task in tasks:
            task.delay = 0
        for delay_combinations in product(range(1, threshold), repeat=number_of_tasks):
            for i, delay in zip(task_combinations, delay_combinations):
                tasks[i].delay = delay
            if calc():
                current_length = max_section(timeline(), target_number_of_tasks)
                if current_length > max_length:
                    max_length = current_length
                    print(max_length, {i+1: tasks[i].delay for i in task_combinations}, timeline())