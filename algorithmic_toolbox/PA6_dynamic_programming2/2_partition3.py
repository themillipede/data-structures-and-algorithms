# Uses python3

"""
2. Partitioning Souvenirs

Task: You and two of your friends have just returned back home after visiting various countries. Now you would like
    to split evenly all the souvenirs that all three of you bought, so each person receives the same value of items.

Input: The first line contains an integer n -- the number of souvenirs. The second line contains n integers
    v_1, v_2, ..., v_n separated by spaces, where v_i is the value of the i-th souvenir.

Constraints: 1 <= n <= 20; 1 <= v_i <= 30 for all i.

Output: 1 if it is possible to partition v_1, v_2, ..., v_n into three subsets with equal sums, and 0 otherwise.
"""

import sys


def partition3(item_weights):
    num_items = len(item_weights)
    subset_sum = sum(item_weights) / 3

    # If the total value is not divisible by 3, or any of the items
    # have more than a third of the total souvenir value, return 0.
    if subset_sum % 1 != 0 or max(item_weights) > subset_sum:
        return 0
    subset_sum = int(subset_sum)

    # Indices for the items, subset 1, and subset 2 (subset 3 is automatically defined based on subsets 1 and 2).
    value = [[[False for _ in range(subset_sum + 1)] for _ in range(subset_sum + 1)] for _ in range(num_items + 1)]
    # Having considered none of the items yet for subsets 1 and 2, a division is possible (i.e. subset 3 takes all).
    value[0][0][0] = True

    for i in range(1, num_items + 1):
        next_item_weight = item_weights[i - 1]
        for x in range(subset_sum + 1):
            for y in range(subset_sum + 1):
                # If a point (x, y) on the plane specified by index i has value "True", this means that it is
                # possible to form two sets that sum to the values x and y, respectively, using only items in
                # item_weights that have index <= i.

                # x is the current size of subset 1, y is the current size of subset 2, and we want to find out
                # if it is possible to partition this particular set of items into the three subsets. For this,
                # we take the current item, and for the current subset sizes, determine whether it can fit into
                # any of the three subsets, without any other items being discarded.
                value[i][x][y] = ((value[i - 1][x - next_item_weight][y] and next_item_weight <= x) or
                                  (value[i - 1][x][y - next_item_weight] and next_item_weight <= y) or
                                  value[i - 1][x][y]) # The item goes in subset 3.
                # Note that the size of subset 3 is always the sum of all item weights minus (x + y).

    return int(value[num_items][subset_sum][subset_sum])


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
