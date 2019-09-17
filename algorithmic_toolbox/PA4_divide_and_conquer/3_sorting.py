# Uses python3

"""
3. Improving quick sort

Introduction: The goal in this problem is to redesign the randomized quick sort algorithm so that it works
    fast even on sequences containing many equal elements.

Task: Replace the 2-way partition with a 3-way partition to enable the quick sort algorithm to efficiently
    process sequences with few unique elements. That is, your new partition procedure should partition the
    array into three parts: < x part, = x part, and > x part.

Input: The first line contains an integer n. The next line contains a sequence of n integers a_0, a_1, ..., a_(n-1).

Constraints: 1 <= n <= 10^5; 1 <= a_i <= 10^9 for all 0 <= i < n.

Output: The sequence sorted in in non-decreasing order.
"""

import sys
import random


#################################
# Quick sort with 2-way partition
#################################

def partition2(a, l, r):
    pivot = a[l]
    p_idx = l
    for i in range(l + 1, r + 1):
        if a[i] <= pivot:
            p_idx += 1
            a[i], a[p_idx] = a[p_idx], a[i]
    a[l], a[p_idx] = a[p_idx], a[l]
    return p_idx


def randomized_quick_sort2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort2(a, l, m - 1)
    randomized_quick_sort2(a, m + 1, r)


#################################
# Quick sort with 3-way partition
#################################

def partition3(a, l, r):
    pivot = a[l]
    p_idx = l
    k = l  # Will become the index of the largest number smaller than the pivot.
    for i in range(l + 1, r + 1):
        if a[i] <= pivot:
            p_idx += 1
            a[i], a[p_idx] = a[p_idx], a[i]
            if a[p_idx] < pivot:
                k += 1
                a[k], a[p_idx] = a[p_idx], a[k]
    a[l], a[p_idx] = a[p_idx], a[l]
    return k, p_idx


def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort3(a, l, m1)
    randomized_quick_sort3(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
