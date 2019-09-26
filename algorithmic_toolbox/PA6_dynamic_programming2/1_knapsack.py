# Uses python3

"""
1. Maximum amount of gold

Introduction: You are given a set of bars of gold and your goal is to put as much gold as possible into your bag.
    For each bar you can either take it or not (i.e. you cannot take a fraction of a bar).

Input: The first line contains the capacity of a knapsack, W, and the number of bars of gold, n. The next line
    contains n integers w_0, w_1, ..., w_(n-1) defining the weights of the bars of gold.

Constraints: 1 <= W <= 10^4; 1 <= n <= 300; 0 <= w_0, ..., w_(n-1) <= 10^5.

Output: The maximum weight of gold that fits into a knapsack of capacity W.
"""

import sys


def optimal_weight_alternative(capacity, item_weights):
    num_items = len(item_weights)
    value = [[0 for _ in range(num_items + 1)] for _ in range(capacity + 1)]
    for i in range(1, num_items + 1):
        next_item_weight = item_weights[i - 1]
        for w in range(1, capacity + 1):
            prev = value[w][i - 1]
            curr = value[w - next_item_weight][i - 1] + next_item_weight
            value[w][i] = prev if curr > w else max(prev, curr)
    return value[-1][-1]


def optimal_weight(capacity, item_weights):
    num_items = len(item_weights)
    # For every possible capacity between 1 and the actual capacity (inclusive),
    # we'll record the maximum possible weight for all items considered so far.
    value = [[0 for _ in range(num_items + 1)] for _ in range(capacity + 1)]
    for i in range(1, num_items + 1):
        next_item_weight = item_weights[i - 1]
        for w in range(1, capacity + 1):  # w is the "intermediate capacity" currently under consideration.
            value[w][i] = value[w][i - 1]  # If we don't include the next item, this will be the weight.
            if next_item_weight <= w:
                # If we include the next item, (w - next_item_weight) is the capacity we'll have
                # remaining. We look up the optimal weight we can fit in this residual capacity.
                # If this value + next_item_weight is greater than the default, then update it.
                val = value[w - next_item_weight][i - 1] + next_item_weight
                if val > value[w][i]:
                    value[w][i] = val
    return value[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
