# Uses python3

"""
1. Money change again

Introduction: As we already know, a natural greedy strategy for the change problem does not work correctly for
    any set of denominations. For example, if the available denominations are 1, 3 and 4, the greedy algorithm
    will change 6 cents using three coins (4 + 1 + 1), while it can be changed using just two coins (3 + 3).
    Your goal is to apply dynamic programming to solve the Money Change Problem for denominations 1, 3, and 4.

Input: Integer money.

Output: The minimum number of coins with denominations 1, 3, 4 that changes money.

Constraints: 1 <= money <= 10^3.
"""

import sys


# Naive recursive solution.
def get_change_recursive(m):
    if m < 1:
        return float('inf')
    if m in (4, 3, 1):
        return 1
    return 1 + min(
        get_change_recursive(m - 4),
        get_change_recursive(m - 3),
        get_change_recursive(m - 1))


# Recursive dynamic programming solution.
def get_change_dp_recursive(m, min_num_coins=None):
    if not min_num_coins:
        min_num_coins = {0: 0}
    if m in min_num_coins:
        return min_num_coins[m]
    if m < 1:
        return float('inf')
    if m in (4, 3, 1):
        return 1
    min_num_coins[m] = 1 + min(
        get_change_dp_recursive(m - 4, min_num_coins),
        get_change_dp_recursive(m - 3, min_num_coins),
        get_change_dp_recursive(m - 1, min_num_coins))
    return min_num_coins[m]


# Iterative dynamic programming solution.
def get_change_dp_iterative(money, min_num_coins=None):
    if not min_num_coins:
        min_num_coins = {0: 0}
    for m in range(1, money + 1):
        min_num_coins[m] = float('inf')
        for i in (1, 3, 4):
            if m >= i:
                num_coins = min_num_coins[m - i] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change_dp_iterative(m))
