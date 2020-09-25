from sorts.radix import radix_sort
import time
from sorts.shuffled_arrays import create_shufled_arrays

sorts = [sorted,
         radix_sort,
         lambda arr: radix_sort(arr, radix=16),
         lambda arr: radix_sort(arr, radix=128),
         lambda arr: radix_sort(arr, radix=256),
         ]

sorts[2].__name__ = 'radix 16'
sorts[3].__name__ = 'radix 128'
sorts[4].__name__ = 'radix 256'


def time_all_sorts_on(arr=None, size=1000000):
    arrays = {}
    if arr:
        arrays['user given'] = arr
        size = len(arr)
    arrays = {**arrays, **create_shufled_arrays(size)}

    print(f'timing on array of length {size}')
    all_words = [*map(lambda x: x.__name__, sorts), 'sort name', *arrays.keys()]
    max_name_len = len(max(all_words, key=len))
    print('sort name'.ljust(max_name_len), end=' | ')
    for name in arrays:
        print(name.ljust(max_name_len), end=' | ')
    print('\n' + '-' * ((max_name_len + 3) * (len(arrays) + 1) - 1))
    for sort in sorts:
        print(sort.__name__.ljust(max_name_len), end=' | ')
        for name in arrays:
            start = time.time()
            sort(arrays[name])
            total_time = time.time() - start
            print(str(round(total_time, 6)).ljust(max_name_len), end=' | ')
        print()


if __name__ == '__main__':
    time_all_sorts_on()
