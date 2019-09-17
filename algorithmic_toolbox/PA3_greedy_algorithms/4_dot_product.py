# Uses python3

"""
3. Maximum advertisement revenue

Introduction: You have n ads to place on a popular Internet page. For each ad, you know how much the advertiser
    is willing to pay for one click on the ad. You have set up n slots on your page and estimated the expected
    number of clicks per day for each slot. Now, your goal is to distribute the ads among the slots to maximize
    the total revenue.

Task: Given two sequences a_1, a_2, ..., a_n and b_1, b_2, ..., b_n (a_i is the profit per click of the i-th ad
    and b_i is the average number of clicks per day of the i-th slot), partition them into n pairs (a_i, b_j)
    such that the sum of their products is maximized.

Constraints: 1 <= n <= 10^3; -10^5 <= a_i, b_i <= 10^5 for all 1 <= i <= n.

Output: The maximum value of SUM[i=1->n](a_i * c_i), where c_1, c_2, ..., c_n is a permutation of b_1, b_2, ..., b_n.
"""

import sys


def max_dot_product(a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    return sum(a_i * b_i for a_i, b_i in zip(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
