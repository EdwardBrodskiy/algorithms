def bubble_sort(arr_in):
    arr = arr_in.copy()

    for i in range(len(arr) - 1):
        swap = False
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
                swap = True
        if not swap:
            break
    return arr


if __name__ == '__main__':
    print(bubble_sort(list(reversed(range(100)))))
