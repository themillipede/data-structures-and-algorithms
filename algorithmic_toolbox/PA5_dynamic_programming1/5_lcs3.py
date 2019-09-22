# Uses python3

"""
4. Longest common subsequence of three sequences

Introduction: The goal in this problem is to compute the length of a longest common subsequence of three sequences.

Task: Given three sequences A = (a_1, a_2, ..., a_n), B = (b_1, b_2, ..., b_m), and C = (c_1, c_2, ..., c_m), find
    the length of their longest common subsequence, i.e. the largest non-negative integer p such that there exist
    indices 1 <= i_1 < i_2 < ... < i_p <= n, 1 <= j_1 < j_2 < ... < j_p <= m, 1 <= k_1 < k_2 < ... < k_p <= l such
    that a_i1 = b_j1 = c_k1, ..., a_ip = b_jp = c_kp.

Input: First line: n. Second line: a_1, a_2, ..., a_n. Third line: m. Fourth line: b_1, b_2, ..., b_m. Fifth line:
    l. Sixth line: c_1, c_2, ..., c_l.

Constraints: 1 <= n, m, l <= 100; -10^9 <= a_i, b_i, c_i <= 10^9.

Output: The length of the longest subsequence, p.
"""

import sys


def lcs3(a, b, c):
    n = len(a) + 1
    m = len(b) + 1
    l = len(c) + 1
    d = [[[0 for _ in range(l)] for _ in range(m)] for _ in range(n)]
    for k in range(1, l):
        for j in range(1, m):
            for i in range(1, n):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    d[i][j][k] = d[i - 1][j - 1][k - 1] + 1
                else:
                    d[i][j][k] = max(d[i][j][k - 1], d[i][j - 1][k], d[i - 1][j][k])
    return d[n - 1][m - 1][l - 1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
