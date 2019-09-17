# Uses python3

"""
5. Maximum number of prizes

Introduction: You are organising a competition for children. As a prize fund you have n candies. You would like to
    use these candies for the top k places in the competition with a natural restriction that a higher place gets
    a larger number of candies. To make as many children happy as possible, you need to find the largest value of
    k for which this is possible.

Task: Represent a given positive integer n as the sum of as many pairwise distinct positive integers as possible.
    That is, find the maximum value k such that n can be written as a_1 + a_2 + ... + a_k where a_1, ..., a_k are
    positive integers and a_i != a_j for all 1 <= i < j <= k.

Input: A single integer n.

Constraints: 1 <= n <= 10^9.

Output: In the first line, output the maximum value of k such that n can be represented as the sum of k pairwise
    distinct positive integers. In the second line, output k pairwise distinct positive integers that sum up to n
    (if there are many such representations, output any of them).
"""

import sys


def optimal_summands(n):
    summands = []
    curr_total = 0
    last_value = 1
    while n >= curr_total + last_value:
        summands.append(last_value)
        curr_total += last_value
        last_value += 1
    summands[-1] += (n - curr_total)
    return summands


if __name__ == '__main__':
    n = int(sys.stdin.read())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
