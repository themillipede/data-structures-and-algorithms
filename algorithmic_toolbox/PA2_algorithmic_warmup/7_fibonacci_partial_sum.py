# Uses python3

"""
7. Last digit of the sum of Fibonacci numbers again

Task: Given two non-negative integers m and n, where m <= n, find the last digit of the sum
    of all Fibonacci numbers between the m-th and n-th Fibonacci numbers, inclusive.

Input: Two non-negative integers m and n on the same line (separated by a space).

Constraints: 0 <= m <= n <= 10^18.

Output: The last digit of F_m + F_(m+1) + ... + F_n, where F_n is the n-th Fibonacci number.
"""

import sys


# Naive solution.
def fibonacci_partial_sum_naive(first, last):
    sum = 0
    curr = 0
    next = 1
    for i in range(last + 1):
        if i >= first:
            sum += curr
        curr, next = next, curr + next
    return sum % 10


# Efficient solution.
def fibonacci_partial_sum(first, last):
    return (fibonacci_sum(last) - fibonacci_sum(first - 1)) % 10


def fibonacci_sum(n):
    pisano_period = get_pisano_period(10)
    num_periods = (n + 1) // len(pisano_period)
    remainder = (n + 1) % len(pisano_period)
    return (num_periods * sum(pisano_period) + sum(pisano_period[:remainder])) % 10


def get_pisano_period(m):
    pisano_period = []
    n = 2
    prev = 0
    curr = 1
    while pisano_period[-2:] != [0, 1]:
        prev, curr = curr, prev + curr
        pisano_period.append(curr % m)
        n += 1
    return pisano_period[-2:] + pisano_period[:-2]


if __name__ == '__main__':
    input = sys.stdin.read()
    first, last = map(int, input.split())
    print(fibonacci_partial_sum(first, last))
