# Uses python3


def calc_fib_naive(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib(n):
    curr = 0
    next = 1
    i = 0
    while i < n:
        curr, next = next, curr + next
        i += 1
    return curr


n = int(input())
print(calc_fib(n))
