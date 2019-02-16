# Uses python3
import sys

# 1. Money Change
# Task: Find the minimum number of coins with denominations
# 1, 5, and 10 needed to change an integer value of money m
# Constraints: 1 <= m <= 10^3


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
