# Uses python3

"""
4. Longest common subsequence of two sequences

Introduction: The goal in this problem is to compute the length of a longest common subsequence of two sequences.

Task: Given two sequences A = (a_1, a_2, ..., a_n) and B = (b_1, b_2, ..., b_m), find the length of their longest
    common subsequence, i.e. the largest non-negative integer p such that there exist indices
    1 <= i_1 < i_2 < ... < i_p <= n and 1 <= j_1 < j_2 < ... < j_p <= m, such that a_i1 = b_j1, ..., a_ip = b_jp.

Input: First line: n. Second line: a_1, a_2, ..., a_n. Third line: m. Fourth line: b_1, b_2, ..., b_m.

Constraints: 1 <= n, m <= 100; -10^9 <= a_i, b_i <= 10^9.

Output: The length of the longest subsequence, p.
"""

import sys


def lcs2(seq_a, seq_b):
    n = len(seq_a) + 1
    m = len(seq_b) + 1
    D = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(1, m):
        for i in range(1, n):
            if seq_a[i - 1] == seq_b[j - 1]:  # i-th element of seq_a and j-th element of seq_b will add to LCS.
                D[i][j] = D[i - 1][j - 1] + 1
            else:                             # LCS has already been identified.
                D[i][j] = max(D[i][j - 1], D[i - 1][j])
    return D[n - 1][m - 1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
