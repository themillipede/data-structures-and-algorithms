# python3

"""
4.Construct the suffix array of a string

Introduction: We've seen that suffix trees can be too memory intensive to apply in practice. This becomes a serious
    issue for the case of massive datasets like those arising in bioinformatics. In 1993, Udi Manber and Gene Myers
    introduced suffix arrays as a memory-efficient alternative to suffix trees. To construct SuffixArray(Text),
    we first sort all suffixes of Text lexicographically, assuming that "$" comes first in the alphabet. The suffix
    array is the list of starting positions of these sorted suffixes. For example, SuffixArray("panamabananas$") is
    (13, 5, 3, 1, 7, 9, 11, 6, 4, 2, 8, 10, 0, 12). To put this into perspective, the suffix tree of a human genome
    requires about 60 Gb, while the suffix array occupies around 12 Gb.

Task: Construct the suffic array of a string.

Constraints: 1 <= |Text| <= 10^4; except for the last symbol, Text contains symbols A, C, G, T only.

Output: SuffixArray(Text), that is, the list of starting positions (0-based) of sorted suffixes separated by spaces.
"""

import sys


def build_suffix_array(text):
    """
    Build suffix array of the string text and return a list result of the same
    length as the text such that the value result[i] is the index (0-based) in
    text where the i-th lexicographically smallest suffix of text starts.
    """
    sorted_suffixes = sorted([(text[i:], i) for i, _ in enumerate(text)])
    result = [i[1] for i in sorted_suffixes]
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
