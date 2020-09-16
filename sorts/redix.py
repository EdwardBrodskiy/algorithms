def redix_sort(arr):
    digits = len(str(max(arr)))

    arr = list(map(lambda x: str(x).rjust(digits, '0'), arr))

    output = [0 for _ in arr]

    for digit_pos in reversed(range(digits)):

        counts = [0 for _ in range(10)]

        for num in arr:
            counts[int(str(num)[digit_pos])] += 1

        for i in range(len(counts) - 1):
            counts[i + 1] += counts[i]

        for num in reversed(arr):
            digit = int(num[digit_pos])
            counts[digit] -= 1
            output[counts[digit]] = num

        arr = output.copy()

    arr = list(map(lambda x: int(x), arr))

    return arr
