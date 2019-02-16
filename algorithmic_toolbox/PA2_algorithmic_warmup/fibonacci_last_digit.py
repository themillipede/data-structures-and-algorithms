# Uses python3
import sys

# 2. Last digit of a large Fibonacci number
# Task: Given an integer n, find the last digit of the nth Fibonacci number F_n
# Constraints: 0 <= n <= 10^7


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % 10


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_fibonacci_last_digit(n))
