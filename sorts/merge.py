def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    half = len(arr) // 2
    lhalf = merge_sort(arr[:half])
    rhalf = merge_sort(arr[half:])
    return merge(lhalf, rhalf)


def merge(a, b):
    ai, bi = 0, 0
    output = []
    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            output.append(a[ai])
            ai += 1
        else:
            output.append(b[bi])
            bi += 1
    while ai < len(a):
        output.append(a[ai])
        ai += 1
    while bi < len(b):
        output.append(b[bi])
        bi += 1
    return output
