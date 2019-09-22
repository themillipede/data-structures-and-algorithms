# Uses python3

"""
3. Maximum value of an arithmetic expression

Introduction: The goal in this problem is to add parentheses to a given arithmetic expression to maximize its value.

Task: Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic
    operations using additional parentheses.

Input: The only line of the input contains a string s of length 2n + 1 for some n, with symbols s_0, s_1, ..., s_2n.
    Each symbol at an odd position is one of three operations from {+, -, *}.

Constraints: 1 <= n <= 14 (hence the string contains at most 29 symbols).

Output: The maximum possible value of the given arithmetic expression from different orders of applying arithemetic
    operations.
"""


def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_and_max(i, j, minarr, maxarr, operator):
    minval = float('inf')
    maxval = float('-inf')
    for k in range(i, j):
        op = operator[k - 1]
        a = evaluate(maxarr[i][k], maxarr[k + 1][j], op)
        b = evaluate(maxarr[i][k], minarr[k + 1][j], op)
        c = evaluate(minarr[i][k], maxarr[k + 1][j], op)
        d = evaluate(minarr[i][k], minarr[k + 1][j], op)
        minval = min(minval, a, b, c, d)
        maxval = max(maxval, a, b, c, d)
    return minval, maxval


def parentheses(n, minarr, maxarr, digit, operator):
    for i in range(1, n + 1):
        minarr[i][i] = digit[i - 1]
        maxarr[i][i] = digit[i - 1]
    for s in range(1, n):
        for i in range(1, n - s + 1):
            j = i + s
            minarr[i][j], maxarr[i][j] = min_and_max(i, j, minarr, maxarr, operator)
    return maxarr[1][n]


def get_maximum_value(dataset):
    digit = [int(c) for i, c in enumerate(dataset) if i % 2 == 0]
    operator = [c for i, c in enumerate(dataset) if i % 2 == 1]
    minarr = [[0 for _ in range(len(digit) + 1)] for _ in range(len(digit) + 1)]
    maxarr = [[0 for _ in range(len(digit) + 1)] for _ in range(len(digit) + 1)]
    n = len(digit)
    return parentheses(n, minarr, maxarr, digit, operator)


if __name__ == "__main__":
    print(get_maximum_value(input()))
