# Uses python3

"""
4. Number of inversions

Introduction: An inversion of a sequence a_0, a_1, ..., a_n is a pair of indices 0 <= i < j < n such that a_i > a_j.
    The number of inversions of a sequence in some sense measures how close the sequence is to being sorted. For
    example, a sequence sorted in non-descending order contains no inversions at all, while in a sequence sorted in
    descending order any two elements constitute an inversion (for a total of n(n - 1)/2 inversions).

Task: Count the number of inversions in a given sequence.

Input: The first line contains an integer n. The next line contains a sequence of integers a_0, a_1, ..., a_(n-1).

Constraints: 1 <= n <= 10^5; 1 <= a_i <= 10^9; for all 0 <= i <= n.

Output: The number of inversions in the sequence.
"""

import sys


def get_number_of_inversions(A):
    if len(A) <= 1:
        return A, 0
    mid = len(A) // 2
    X, x_inversions = get_number_of_inversions(A[:mid])
    Y, y_inversions = get_number_of_inversions(A[mid:])
    Z, z_inversions = merge_count_inversions(X, Y)
    return Z, (x_inversions + y_inversions + z_inversions)


def merge_count_inversions(X, Y):
    Z = []
    num_inversions = 0
    x_idx, y_idx = 0, 0
    while len(X) > x_idx and len(Y) > y_idx:
        if Y[y_idx] < X[x_idx]:
            num_inversions += len(X[x_idx:])
            Z.append(Y[y_idx])
            y_idx += 1
        else:
            Z.append(X[x_idx])
            x_idx += 1
    Z += X[x_idx:]
    Z += Y[y_idx:]
    return Z, num_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a)[1])
