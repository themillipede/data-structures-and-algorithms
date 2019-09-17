# Uses python3

"""
1. Money change

Task: Given an integer m, find the minimum number of coins needed to change money with value m into coins with
    denominations 1, 5, and 10.

Input: A single integer m.

Constraints: 1 <= m <= 10^3.

Output: The minimum number of coins with denominations 1, 5, and 10 needed to change money with value m.
"""

import sys


def get_change(m):
    count = 0
    if m >= 10:
        count += m // 10
        m %= 10
    if m >= 5:
        count += m // 5
        m %= 5
    count += m
    return count


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
