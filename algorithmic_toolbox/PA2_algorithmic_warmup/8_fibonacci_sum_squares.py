# Uses python3

"""
8. Last digit of the sum of squares of Fibonacci numbers

Task: Given an integer n, find the last digit of the sum of squares of the first n Fibonacci numbers.

Input: A single integer n.

Constraints: 0 <= n <= 10^18.

Output: The last digit of (F_0)^2 + (F_1)^2 + ... + (F_n)^2, where F_n is the nth Fibonacci number.
"""

import sys


# Naive solution.
def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    sum = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
        sum += curr * curr
    return sum % 10


# Efficient solution.
def fibonacci_sum_squares(n):
    return (get_fibonacci_huge(n, 10) * get_fibonacci_huge(n + 1, 10)) % 10


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


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(fibonacci_sum_squares(n))
