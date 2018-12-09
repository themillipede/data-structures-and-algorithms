# Uses python3
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
    value = [[0 for _ in range(num_items + 1)] for _ in range(capacity + 1)]
    for i in range(1, num_items + 1):
        next_item_weight = item_weights[i - 1]
        for w in range(1, capacity + 1):
            value[w][i] = value[w][i - 1]
            if next_item_weight <= w:
                val = value[w - next_item_weight][i - 1] + next_item_weight
                if val > value[w][i]:
                    value[w][i] = val
    return value[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
