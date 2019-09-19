# python3

"""
1. Construct the Burrows-Wheeler transform of a string

Introduction: The Burrows-Wheeler transform of a string Text permutes the symbols of Text so that it becomes well
    compressible. Moreover, the transformation is reversible: one can recover the initial string Text from its
    Burrows-Wheeler transform. However, data compression is not its only application: it is also used for solving
    the multiple pattern matching problem and the sequence alignment problem. BWT(Text) is defined as follows.
    First, form all possible cyclic rotations of Text; a cyclic rotation is defined by chopping off a suffix from
    the end of Text and appending this suffix to the beginning of Text. Then, order all the cyclic rotations of
    Text lexicographically to form a |Text| x |Text| matrix of symbols, denoted by M(Text). BWT(Text) is the last
    column of M(Text).

Task: Construct the Burrows-Wheeler transform of a string.

Input: A string Text ending with a "$" symbol.

Constraints: 1 <= |Text| <= 1000; except for the last symbol, Text contains symbols A, C, G, T only.

Output: BWT(Text)
"""

import sys


def burrows_wheeler_transform(text):
    rotations = [text[i:] + text[:i] for i in range(len(text), 0, -1)]
    rotations.sort()
    bwt = ''.join([string[-1] for string in rotations])
    return bwt


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(burrows_wheeler_transform(text))
