#Uses python3

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
