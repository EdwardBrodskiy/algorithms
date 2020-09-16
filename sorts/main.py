from sorts.redix import redix_sort
import time
import random

sorts = [sorted, redix_sort]


def time_all_sorts_on(arr=None):
    if not arr:
        arr = list(range(100000))
        random.shuffle(arr)
    print(f'timing on array of length {len(arr)} which is {arr}')
    for sort in sorts:
        start = time.time()
        sort(arr)
        total_time = time.time() - start
        print(f'{sort.__name__} took {total_time} seconds')


if __name__ == '__main__':
    time_all_sorts_on()
