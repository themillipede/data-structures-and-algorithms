# Uses python3

"""
3. Edit distance

Introduction: The edit distance between two strings is the minimum number of operations (insertions, deletions,
    and substitutions of symbols) to transform one string into another. It is a measure of similarity of two
    strings. Edit distance has applications, for example, in computational biology, natural language processing,
    and spell checking. Your goal in this problem is to compute the edit distance between two strings.

Task: Implement an algorithm for computing the edit distance between two strings.

Input: Each of the two lines of the input contains a string consisting of lower case latin letters.

Constraints: The length of both strings is at least 1 and at most 100.

Output: The edit distance between the given two strings.
"""


def edit_distance(string1, string2):
    n = len(string1) + 1
    m = len(string2) + 1
    D = [[0 for _ in range(m)] for _ in range(n)]  # Construct an n x m grid.
    for i in range(n):
        D[i][0] = i  # The edit distance from the null string to string1[:i].
    for j in range(m):
        D[0][j] = j  # The edit distance from the null string to string2[:j].
    for j in range(1, m):
        for i in range(1, n):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1
            if string1[i - 1] == string2[j - 1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return D[n - 1][m - 1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
