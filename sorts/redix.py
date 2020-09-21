def redix_sort(arr, redix=10):
    digits = len(str(max(arr)))

    output = [0 for _ in arr]

    for digit_pos in reversed(range(digits)):

        counts = [0 for _ in range(redix)]

        for num in arr:
            counts[num // redix ** digit_pos % redix] += 1

        for i in range(len(counts) - 1):
            counts[i + 1] += counts[i]

        for num in reversed(arr):
            digit = num // redix ** digit_pos % redix
            counts[digit] -= 1
            output[counts[digit]] = num

        arr = output.copy()

    return arr
