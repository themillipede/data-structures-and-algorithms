# Uses python3

"""
2. Primitive calculator

Introduction: You are given a primitive calculator that can perform the following three operations with the current
    number x: multiply x by 2, multiply x by 3, or add 1 to x. Your goal is: given a positive integer n, find the
    minimum number of operations needed to obtain the number n starting from the number 1.

Task: Given an integer n, compute the minimum number of operations needed to obtain the number n from the number 1.

Input: A single integer n.

Constraints: 1 <= n <= 10^6.

Output: On the first line, output the minimum number of operations k needed to get n from 1. On the second line,
    output a sequence of intermediate numbers. That is, the second line should contain positive integers
    a_0, a_1, ..., a_(k --1) such that a_0 = 1, a_(k-1) = n, and for all 0 <= i < k - 1, a_(i+1) is equal to
    either a_i + 1, 2a_i, or 3a_i. If there are many such sequences, output any one of them.
"""

import sys


# Recursively finds k, but not the sequence leading to k.
def optimal_sequence_minimum_steps(n, min_num_steps=None):
    if not min_num_steps:
        min_num_steps = {1: 0}
    if n in min_num_steps:
        return min_num_steps[n]
    elif n % 1 != 0 or n < 1:
        return float('inf')
    else:
        min_num_steps[n] = 1 + min(
            optimal_sequence_minimum_steps(n / 3, min_num_steps) if n % 3 == 0 else float('inf'),
            optimal_sequence_minimum_steps(n / 2, min_num_steps) if n % 2 == 0 else float('inf'),
            optimal_sequence_minimum_steps(n - 1, min_num_steps))
        return min_num_steps[n]


# Full dynamic programming solution.
def optimal_sequence(n):
    sequence = []
    a = [0 for _ in range(n + 1)]
    for i in range(1, len(a)):
        a[i] = a[i - 1] + 1
        if i % 2 == 0:
            a[i] = min(1 + a[i // 2], a[i])
        if i % 3 == 0:
            a[i] = min(1 + a[i // 3], a[i])
    while n >= 1:
        sequence.append(n)
        if a[n - 1] == a[n] - 1:
            n -= 1
        elif n % 2 == 0 and a[n // 2] == a[n] - 1:
            n //= 2
        elif n % 3 == 0 and a[n // 3] == a[n] - 1:
            n //= 3
    return reversed(sequence)


n = int(sys.stdin.read())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
