from itertools import zip_longest


class BigFloat:
    def __init__(self, num):
        self.num: str = str(float(num))
        self.dp_index = self.num.find('.')

    def __iadd__(self, other):
        if type(other) == type(self):
            carry = 0
            for us, it in reversed(zip_longest(self.num, other.num)):
                if us and it:
                    pass
