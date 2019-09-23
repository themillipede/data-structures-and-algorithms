# Uses python3

"""
3. Greatest common divisor

Task: Given two integers a and b, find their greatest common divisor.

Input: Two integers a and b on the same line (separated by a space).

Constraints: 1 <= a, b <= 2*10^9.

Output: The greatest common divisor of a and b.
"""

import sys


# Naive solution.
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    return current_gcd


# Efficient solution.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
