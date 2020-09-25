def radix_sort(arr, radix=10):
    digits = len(str(max(arr)))

    output = [0 for _ in arr]

    for digit_pos in reversed(range(digits)):

        counts = [0 for _ in range(radix)]

        for num in arr:
            counts[num // radix ** digit_pos % radix] += 1

        for i in range(len(counts) - 1):
            counts[i + 1] += counts[i]

        for num in reversed(arr):
            digit = num // radix ** digit_pos % radix
            counts[digit] -= 1
            output[counts[digit]] = num

        arr = output.copy()

    return arr
