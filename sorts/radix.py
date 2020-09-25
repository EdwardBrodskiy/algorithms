def radix_sort(arr, radix=10):
    arr_in = arr.copy()

    digits = len(str(max(arr_in)))

    output = [0 for _ in arr_in]

    for digit_pos in reversed(range(digits)):

        counts = [0 for _ in range(radix)]

        for num in arr_in:
            counts[num // radix ** digit_pos % radix] += 1

        for i in range(len(counts) - 1):
            counts[i + 1] += counts[i]

        for num in reversed(arr_in):
            digit = num // radix ** digit_pos % radix
            counts[digit] -= 1
            output[counts[digit]] = num

        arr_in = output.copy()

    return arr_in


if __name__ == '__main__':
    print(radix_sort(list(reversed(range(100))), radix=16))