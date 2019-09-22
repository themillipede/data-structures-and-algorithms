# python3

"""
1. Find all occurrences of a pattern in a string

Introduction: In this problem, we ask a simple question: how many times does one string occur as a substring of
    another? Recall that different occurrences of a substring can overlap with each other, e.g. ATA occurs three
    times in CGATATATCCATAG. This is a classical pattern matching problem in Computer Science solved millions of
    times per day when computer users use the common "Find" feature in text/code editors and Internet browsers.

Task: Find all occurrences of a pattern in a string.

Input: Strings Pattern and Genome.

Constraints: 1 <= |Pattern| <= 10^6; 1 <= |Genome| <= 10^6; both strings contain only the symbols A, C, G, T.

Output: All starting positions in Genome where Pattern appears as a substring (using 0-based indexing as usual).
"""

import sys


def compute_prefix_function(pattern):
    prefix_function = [0 for _ in pattern]
    border = 0
    for i in range(1, len(pattern)):
        while border > 0 and pattern[i] != pattern[border]:
            border = prefix_function[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        prefix_function[i] = border
    return prefix_function


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text and return
    a list of all positions in the text where the pattern starts.
    """
    result = []
    combined_string = pattern + '$' + text
    prefix_function = compute_prefix_function(combined_string)
    for i in range(len(pattern) + 1, len(combined_string)):
        if prefix_function[i] == len(pattern):
            result.append(i - 2 * len(pattern))
    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
