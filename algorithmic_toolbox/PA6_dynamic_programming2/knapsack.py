# Uses python3
import sys


def optimal_weight_alternative(capacity, item_weights):
    num_items = len(item_weights)
    value = [[0 for _ in range(num_items + 1)] for _ in range(capacity + 1)]
    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            prev = value[w][i - 1]
            curr = item_weights[i - 1] + value[capacity - item_weights[i - 1]][i - 1]
            value[w][i] = prev if curr > w else max(prev, curr)
    return value[-1][-1]


def optimal_weight(capacity, item_weights):
    num_items = len(item_weights)
    value = [[0 for _ in range(num_items + 1)] for _ in range(capacity + 1)]
    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            value[w][i] = value[w][i - 1]
            if item_weights[i - 1] < w:
                val = value[capacity - item_weights[i - 1]][i - 1] + item_weights[i - 1]
                if value[w][i] < val:
                    value[w][i] = val
    return value[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
