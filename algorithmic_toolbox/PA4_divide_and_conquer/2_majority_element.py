# Uses python3

"""
2. Majority element

Introduction: Majority rule is a decision rule that selects the alternative which has a majority, that is, more
    than half of the votes. Given a sequence of elements a_1, a_2, ..., a_n, you would like to check whether it
    contains an element that appears more than n/2 times. Your goal is to use the divide-and-conquer technique
    to design an O(nlogn) algorithm.

Task: Check whether an input sequence contains a majority element.

Input: The first line contains an integer n. The next line contains a sequence of n non-negative integers
    a_0, a_1, ..., a_(n-1).

Constraints: 1 <= n <= 10^5; 0 <= a_i <= 10^9 for all 0 <= i < n.

Output: 1 if the sequence contains an element that appears strictly more than n/2 times, and 0 otherwise.
"""

import sys


def get_majority_element(int_array, left, right):
    if left == right:
        return -1
    if left + 1 == right:  # Only one element, so that element is the majority element.
        return a[left]
    mid = (left + right) // 2
    majority_left = get_majority_element(int_array, left, mid)
    majority_right = get_majority_element(int_array, mid, right)
    if majority_left == majority_right:
        return majority_left
    if majority_left != -1:  # The left half has a majority element.
        count = sum(i == majority_left for i in int_array[left:right])  # Check if majority over left + right.
        if count > (right - left) // 2:
            return majority_left
    if majority_right != -1:  # The right half has a majority element.
        count = sum(i == majority_right for i in int_array[left:right]) # Check if majority over left + right.
        if count > (right - left) // 2:
            return majority_right
    return -1


# Algorithm that runs in linear
# time and uses constant space.
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
