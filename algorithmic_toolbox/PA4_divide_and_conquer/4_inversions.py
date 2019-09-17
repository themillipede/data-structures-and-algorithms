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


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    X = a[left:ave] if ave - left <= 1 else b[left:ave]
    Y = a[ave:right] if right - ave <= 1 else b[ave:right]
    x, y = 0, 0
    b_index = left
    while x < len(X) and y < len(Y):
        if Y[y] < X[x]:
            number_of_inversions += len(X[x:])
            b[b_index] = Y[y]
            y += 1
        else:
            b[b_index] = X[x]
            x += 1
        b_index += 1
    if x < len(X):
        b[b_index:right] = X[x:]
    else:
        b[b_index:right] = Y[y:]

    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
