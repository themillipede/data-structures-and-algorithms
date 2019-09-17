# Uses python3

"""
2. Maximum value of the loot

Introduction: A thief finds much more loot than is bag can fit. Help him to find the most valuable combination of
    items assuming that any fraction of a loot item can be put into his bag.

Task: Implement an algorithm for the fractional knapsack problem.

Input: The first line contains the number of items n and the capacity W of a knapsack. The next n lines define the
    values and weights of the items. The i-th line contains integers v_i and w_i -- the value and the weight of the
    i-th item, respectively.

constraints: 1 <= n <= 10^3; 0 <= W <= 2*10^6; 0 <= v_i <= 2*10^6; 0 <= w_i <= 2*10^6 for all 1 <= i <= n. All the
    numbers are integers.

Output: The maximal value of fractions of items that fit into the knapsack. The absolute value of the difference
    between the answer of your program and the optimal value should be at most 10^-3.
"""

import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    value_per_weight = [(i, values[i] / weights[i]) for i, _ in enumerate(values)]
    value_per_weight.sort(key=lambda x: x[1], reverse=True)
    i = 0
    while capacity > 0 and i < len(values):
        j = value_per_weight[i][0]
        if weights[j] <= capacity:
            value += values[j]
            capacity -= weights[j]
        else:
            value += capacity * value_per_weight[i][1]
            capacity = 0
        i += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
