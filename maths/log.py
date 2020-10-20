from decimal import Decimal


def log(num, base=2):
    result = 0
    while num > base:
        num /= base
        result += 1

    two_to_the_power_of_n = 1
    prev_result = 0
    while prev_result != result:
        num *= num
        two_to_the_power_of_n /= 2
        if num > base:
            prev_result = result
            result += two_to_the_power_of_n
            num /= base

    return result


def precise_log(num, base=2):
    if type(num) != Decimal:
        num = Decimal(num)
    result = Decimal(0)
    while num > base:
        num /= base
        result += 1
    two_to_the_power_of_n = Decimal(1)
    prev_result = 0
    while prev_result != result:
        num *= num
        two_to_the_power_of_n /= 2
        if num > base:
            prev_result = result
            result += two_to_the_power_of_n
            num /= base
    return result


if __name__ == '__main__':
    print(f'log2(10) = {log(10)}')
    print(f'Precise log2(10) = {precise_log(10)}')
