# Uses python3
import sys

# 4. Least common multiple
# Task: Given two integers a and b, find their lowest common multiple
# Constraints: 1 <= a, b <= 2 * 10^9


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a * b


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    gcd_ab = gcd(a, b)
    return a * b / gcd_ab


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

