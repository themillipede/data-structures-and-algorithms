# Uses python3

# 1. Fibonacci number
# Task: Given an integer n, find the nth Fibonacci number F_n
# Constraints: 0 <= n <= 45


def calc_fib_naive(n):
    if n <= 1:
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
