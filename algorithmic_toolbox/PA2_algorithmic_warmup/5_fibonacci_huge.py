# Uses python3

"""
5. Fibonacci number again

Task: Given two integers n and m, find F_n mod m, where F_n is the n-th Fibonacci number.

Input: Two integers n and m on the same line (separated by a space).

Constraints: 1 <= n <= 10^18, 2 <= m <= 10^3.

Output: F_n mod m.
"""

import sys


# Naive solution.
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr % m


# Efficient solution.
def get_fibonacci_huge(n, m):
    len_pisano_period = get_length_of_pisano_period(m)
    remainder = n % len_pisano_period
    return get_fibonacci(remainder) % m


def get_length_of_pisano_period(m):
    pisano_period = []
    n = 2
    prev = 0
    curr = 1
    while pisano_period[-2:] != [0, 1]:
        prev, curr = curr, prev + curr
        pisano_period.append(curr % m)
        n += 1
    return len(pisano_period)


def get_fibonacci(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


# More compact efficient solution.
def get_fibonacci_huge_alternative(n, m):
    pisano_period = []
    fib_numbers = [0, 1]
    i = 2
    prev = 0
    curr = 1
    while pisano_period[-2:] != [0, 1]:
        prev, curr = curr, prev + curr
        pisano_period.append(curr % m)
        fib_numbers.append(curr)
        i += 1
    remainder = n % len(pisano_period)
    return fib_numbers[remainder] % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
