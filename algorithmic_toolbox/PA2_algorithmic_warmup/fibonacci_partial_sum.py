# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next  = 1
    for i in range(to + 1):
        if i >= from_:
            sum += current
        current, next = next, current + next
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


def fibonacci_partial_sum(from_, to):
    return (fibonacci_sum(to) - fibonacci_sum(from_ - 1)) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))