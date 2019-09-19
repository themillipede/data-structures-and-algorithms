# python3

"""
3. Matching against a compressed string

Introduction: Not only does the Burrows-Wheeler transform make the input string Text well compressible, it also
    allows one to solve the pattern matching problem using the compressed strings instead of the initial string!
    This is another beautiful property of the Burrows-Wheeler transform, which allows us to avoid decompressing
    the string, and thus save lots of memory, while still solving the problem at hand.

Task: Implement the better matching algorithm.

Input: A string BWT(Text), followed by an integer n and a collection of n strings Patterns = {p_1, ..., p_n}
    (on one line separated by spaces).

Constraints: 1 <= |BWT(Text)| <= 10^6; except for the one $ symbol, BWT(Text) contains symbols A, C, G, T only;
    1 <= n <= 5000; for all 1 <= i <= n, p_i is a string over A, C, G, T; 1 <= |p_i| <= 1000.

Output: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th
    member of Patterns in Text.
"""

import sys


def preprocess_bwt(bwt):
    """
    Preprocess the Burrows-Wheeler transform, bwt, of some text and compute as a result:
    - starts: for each character C in bwt, starts[C] is the first position of that character in the
      sorted array of all characters of the text.
    - occ_counts_before: for each character C in bwt and each position P in bwt, occ_count_before[C][P]
      is the number of occurrences of character C in bwt from position 0 to position P inclusive.
    """
    first_column = sorted(bwt)
    starts = {}
    last_char = None
    for i, char in enumerate(first_column):
        if char != last_char:
            starts[char] = i
            last_char = char
    occ_counts_before = {c: {i: 0 for i in range(len(bwt) + 1)} for c in starts}

    for i, char in enumerate(bwt, start=1):
        occ_counts_before[char][i] = occ_counts_before[char][i - 1] + 1
        for c in starts:
            if c != char:
                occ_counts_before[c][i] = occ_counts_before[c][i - 1]

    return starts, occ_counts_before


def count_occurrences(pattern, bwt, starts, occ_counts_before):
    """
    Compute the number of occurrences of string pattern in the text given only the
    Burrows-Wheeler transform bwt of the text and the additional information we
    get from the preprocessing stage -- starts and occ_count_before.
    """
    top = 0
    bottom = len(bwt) - 1
    i = len(pattern) - 1
    while top <= bottom:
        if i > -1:
            symbol = pattern[i]
            i -= 1
            if (symbol in occ_counts_before and
                    occ_counts_before[symbol][bottom + 1] - occ_counts_before[symbol][top] > 0):
                top = starts[symbol] + occ_counts_before[symbol][top]
                bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1
    return 0


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before. For each pattern,
    # we will then use these precomputed values and spend only O(|pattern|) to find
    # all occurrences of the pattern in the text, instead of O(|pattern| + |text|).
    starts, occ_counts_before = preprocess_bwt(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(count_occurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
