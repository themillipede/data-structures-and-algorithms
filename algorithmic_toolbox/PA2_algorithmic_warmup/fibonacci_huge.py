# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m


def get_fibonacci(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


def get_pisano_period(m):
    pisano_period = []
    n = 2
    while pisano_period[-2:] != [0, 1]:
        fib_n = get_fibonacci(n)
        pisano_period.append(fib_n % m)
        n += 1
    return len(pisano_period)


def get_fibonacci_huge(n, m):
    len_pisano_period = get_pisano_period(m)
    remainder = n % len_pisano_period
    return get_fibonacci(remainder) % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
