import random
from arraysearch import constants


def get_random_list(size, interval=constants.INTERVAL_VALUE):
    answer = [1]
    while len(answer) < size:
        answer.append(answer[-1] + random.randint(0, interval))
    return answer


def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)
