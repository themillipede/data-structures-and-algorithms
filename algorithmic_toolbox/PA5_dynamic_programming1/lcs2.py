# Uses python3
import sys


def lcs2(a, b):
    n = len(a) + 1
    m = len(b) + 1
    d = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(1, m):
        for i in range(1, n):
            insertion = d[i][j - 1]
            deletion = d[i - 1][j]
            match = d[i - 1][j - 1] + 1
            if a[i - 1] == b[j - 1]:
                d[i][j] = match
            else:
                d[i][j] = max(insertion, deletion)
    return d[n - 1][m - 1]


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
