# Uses python3

"""
2. Last digit of a large Fibonacci number

Task: Given an integer n, find the last digit of the n-th Fibonacci number F_n.

Input: A single integer n.

Constraints: 0 <= n <= 10^7.

Output: The last digit of F_n.
"""

import sys


# Naive solution.
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr % 10


# Efficient solution.
def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10
    return curr


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_fibonacci_last_digit_naive(n))
