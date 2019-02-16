# Uses python3
import sys

# 5. Maximum number of prizes
# Task: Represent a positive integer n as the sum of as
# many pairwise distinct positive integers as possible
# Constraints: 1 <= n <= 10^9


def optimal_summands(n):
    summands = []
    total = 0
    count = 1
    while n - total >= count:
        summands.append(count)
        total += count
        count += 1
    summands[-1] += (n - total)
    return summands


if __name__ == '__main__':
    n = int(sys.stdin.read())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
