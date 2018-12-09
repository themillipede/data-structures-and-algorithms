# Uses python3
import sys


def partition3(item_weights):
    num_items = len(item_weights)
    subset_sum = sum(item_weights) / 3

    if subset_sum % 1 != 0 or max(item_weights) > subset_sum:
        return False
    subset_sum = int(subset_sum)

    value = [[[False for _ in range(subset_sum + 1)] for _ in range(subset_sum + 1)] for _ in range(num_items + 1)]
    value[0][0][0] = True

    for i in range(1, num_items + 1):
        next_item_weight = item_weights[i - 1]
        for x in range(subset_sum + 1):
            for y in range(subset_sum + 1):
                # If a point (x, y) on the plane specified by index i has value "True", this means that it is
                # possible to form two sets that sum to the values x and y, respectively, using only items in
                # item_weights that have index <= i.
                value[i][x][y] = ((value[i - 1][x - next_item_weight][y] and next_item_weight <= x) or
                                  (value[i - 1][x][y - next_item_weight] and next_item_weight <= y) or
                                  value[i - 1][x][y])
    return value[num_items][subset_sum][subset_sum]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
