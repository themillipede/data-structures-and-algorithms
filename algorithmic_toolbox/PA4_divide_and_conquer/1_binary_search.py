# Uses python3

"""
1. Binary search

Task: Implement the binary search algorithm.

Input: The first line contains an integer n and a sequence of n pairwise distinct positive integers in increasing
    order, a_0 < a_1 < ... < a_(n-1). The next line contains an integer k and k positive integers
    b_0, b_1, ..., b_(k-1).

Constraints: 1 <= n, k <= 10^4; 1 <= a_i <= 10^9 for all 0 <= i < n; 1 <= b_j <= 10^9 for all 0 <= j < k.

Output: For all i from 0 to k-1, output an index 0 <= j <= n-1 such that a_j = b_j or -1 if there is no such index.
"""

import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        elif x > a[mid]:
            left = mid + 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
