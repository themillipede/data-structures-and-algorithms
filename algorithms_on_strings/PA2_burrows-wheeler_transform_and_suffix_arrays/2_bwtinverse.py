# python3

"""
2. Reconstruct a string from its Burrows-Wheeler Transform

Introduction: In the previous problem, we introduced the Burrows-Wheeler transform of a string Text. It permutes
    the symbols of Text making it well compressible. However, there would be no sense to this if the process was
    not reversible. Of course, it is reversible, and the goal in this problem is to recover Text from BWT(Text).

Task: Reconstruct a string from its Burrows-Wheeler transform.

Input: A string Transform with a single "$" sign.

Constraints: 1 <= |Transform| <= 1000000; except for the last symbol, Text contains symbols A, C, G, T only.

Output: The string Text such that BWT(Text) = Transform. (There exists a unique such string.)
"""

import sys


def inverse_bwt(bwt):
    last = [(val, i) for i, val in enumerate(bwt)]
    first = sorted(last)
    first_to_last = {f: l for f, l in zip(first, last)}
    next = first[0]
    result = ''
    for _ in range(len(bwt)):
        result += next[0]
        next = first_to_last[next]
    text = result[::-1]
    return text


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(inverse_bwt(bwt))
