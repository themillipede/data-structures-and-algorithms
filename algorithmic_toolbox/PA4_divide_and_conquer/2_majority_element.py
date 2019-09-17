# Uses python3

"""
2. Majority element

Introduction: Majority rule is a decision rule that selects the alternative which has a majority, that is, more
    than half of the votes. Given a sequence of elements a_1, a_2, ..., a_n, you would like to check whether it
    contains an element that appears more than n/2 times. Your goal is to use the divide-and-conquer technique
    to design an O(nlogn) algorithm.

Task: Check whether an input sequence contains a majority element.

Input: The first line contains an integer n. The next line contains a sequence of non-negative integers
    a_0, a_1, ..., a_(n-1).

Constraints: 1 <= n <= 10^5; 0 <= a_i <= 10^9 for all 0 <= i < n.

Output: 1 if the sequence contains an element that appears strictly more than n/2 times, and 0 otherwise.
"""

import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = (left + right) // 2
    ml = get_majority_element(a, left, mid)
    mr = get_majority_element(a, mid, right)
    if ml == mr:
        return ml
    if ml != -1:
        ml_count = sum([1 for i in a[left:right] if i == ml])
        if ml_count > len(a[left:right]) // 2:
            return ml
    if mr != -1:
        mr_count = sum([1 for i in a[left:right] if i == mr])
        if mr_count > len(a[left:right]) // 2:
            return mr
    return -1


def boyer_moore_majority(a):
    m = None
    i = 0
    for x in a:
        if i == 0:
            m = x
            i = 1
        elif m == x:
            i += 1
        else:
            i -= 1
    if sum([1 for x in a if x == m]) > len(a) // 2:
        return m
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
