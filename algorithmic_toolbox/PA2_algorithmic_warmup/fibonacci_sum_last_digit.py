# Uses python3
import sys

# 6. Last digit of the sum of Fibonacci numbers
# Task: Given an integer n, find the last digit of the sum F_0 + F_1 + ... + F_n
# Constraints: 0 <= n <= 10^18


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    sum = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
    return sum % 10


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


def fibonacci_sum(n):
    pisano_period = get_pisano_period(10)
    num_periods = (n + 1) // len(pisano_period)
    remainder = (n + 1) % len(pisano_period)
    return (num_periods * sum(pisano_period) + sum(pisano_period[:remainder])) % 10


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(fibonacci_sum(n))
