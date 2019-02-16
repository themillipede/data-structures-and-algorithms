# Uses python3
import sys

# 3. Maximum advertisement revenue
# Task: Given two sequences a_1, a_2, ..., a_n, and b_1, b_2, ..., b_n, partition
# them into n pairs, (a_i, b_j), such that the sum of their products is maximised
# Constraints: 1 <= n <= 10^3; -10^5 <= a_i, b_i <= 10^5 for all 1 <= i <= n


def max_dot_product(a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
