# Uses python3
import sys

# 2. Maximum value of the loot
# Task: Given n items, each with a specific value and weight, calculate the maximal
# value of fractions of items that can fit into a knapsack of capacity W, by weight


def get_optimal_value(capacity, weights, values):
    value = 0.
    value_per_weight = [(i, values[i] / weights[i]) for i, _ in enumerate(values)]
    value_per_weight.sort(key=lambda x: x[1], reverse=True)
    i = 0
    while capacity > 0 and i < len(values):
        j = value_per_weight[i][0]
        if weights[j] <= capacity:
            capacity_used = weights[j]
            value += values[j]
        else:
            capacity_used = capacity
            value += capacity * value_per_weight[i][1]
        i += 1
        capacity -= capacity_used
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
