#Uses python3

import sys


def is_greater_or_equal_simple(a, b):
    if b == float('-inf'):
        return True
    a = str(a)
    b = str(b)
    if int(a + b) >= int(b + a):
        return True
    return False


def is_greater_or_equal(a, b):
    if b == float('-inf'):
        return True
    a = str(a)
    b = str(b)
    i = 0
    while i < max(len(a), len(b)) and a[i % len(a)] == b[i % len(b)]:
        i += 1
    if int(a[i % len(a)]) >= int(b[i % len(b)]):
        return True
    return False


def largest_number(a):
    res = ""
    while a:
        max_digit = float('-inf')
        for digit in a:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        res += str(max_digit)
        a.remove(max_digit)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
