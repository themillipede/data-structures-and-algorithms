# Uses python3

"""
6. Maximum salary

Introduction: At the end of a successful interview, your boss gives you a few pieces of paper with numbers on it
    and asks you to compose a larger number from these numbers. The resulting number is going to be your salary,
    so you are very interested in maximizing this number. How can you do this?

Task: Compose the largest number possible out of a set of integers.

Input: The first line contains an integer n. The second line contains integers a_1, a_2, ..., a_n.

Constraints: 1 <= n <= 100; 1 <= a_i <= 10^3 for all 1 <= i <= n.

Output: The largest number that can be composed out of a_1, a_2, ..., a_n.
"""

import sys


# Simpler alternative to the function directly below.
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
