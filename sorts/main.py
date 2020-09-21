from sorts.redix import redix_sort
import time
from sorts.shuffled_arrays import create_shufled_arrays

sorts = [sorted,
         redix_sort,
         lambda arr: redix_sort(arr, redix=16),
         lambda arr: redix_sort(arr, redix=128),
         lambda arr: redix_sort(arr, redix=256),
         ]

sorts[2].__name__ = 'redix 16'
sorts[3].__name__ = 'redix 128'
sorts[4].__name__ = 'redix 256'


def time_all_sorts_on(arr=None, size=1000000):
    arrays = {}
    if arr:
        arrays['user given'] = arr
        size = len(arr)
    arrays = {**arrays, **create_shufled_arrays(size)}

    print(f'timing on array of length {size}')
    print('sort name', end='\t')
    for name in arrays:
        print(name, end='\t')
    print('')
    for sort in sorts:
        print(sort.__name__, end='\t')
        for name in arrays:
            start = time.time()
            sort(arrays[name])
            total_time = time.time() - start
            print(round(total_time, 6), end='\t')
        print()



if __name__ == '__main__':
    time_all_sorts_on()
