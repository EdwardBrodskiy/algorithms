from random import randint


def quick_sort(arr):
    if len(set(arr)) > 1:
        pivot = arr[randint(0, len(arr) - 1)]
        less, more = [], []
        for element in arr:
            if element < pivot:
                less.append(element)
            else:
                more.append(element)
        return [*quick_sort(less), *quick_sort(more)]
    return arr
