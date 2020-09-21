import random


def create_shufled_arrays(size, types='*'):
    shufflers = {
        'only once': only_once,
        'reverse': reverse,
        'pure random': pure_random,
        'pure random large': lambda s: pure_random(s, 0, 1000000)
    }
    if types == '*':
        types = shufflers.keys()

    output = {}

    for shuffler in types:
        output[shuffler] = shufflers[shuffler](size)

    return output


def only_once(size):
    arr = list(range(100000))
    random.shuffle(arr)
    return arr


def reverse(size):
    return list(reversed(range(size)))


def pure_random(size, lower=0, upper=1000):
    return [random.randint(lower, upper) for _ in range(size)]
