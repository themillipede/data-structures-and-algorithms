# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    sum = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current
    return sum % 10


def get_fibonacci(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


def get_pisano_period_length(m):
    pisano_period = []
    n = 2
    prev = 0
    curr = 1
    while pisano_period[-2:] != [0, 1]:
        prev, curr = curr, prev + curr
        pisano_period.append(curr % m)
        n += 1
    return len(pisano_period)


def get_fibonacci_huge(n, m):
    len_pisano_period = get_pisano_period_length(m)
    remainder = n % len_pisano_period
    return get_fibonacci(remainder) % m


def fibonacci_sum_squares(n):
    return (get_fibonacci_huge(n, 10) * get_fibonacci_huge(n + 1, 10)) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
