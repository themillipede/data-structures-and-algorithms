# python3

"""
3. Pattern matching with the suffix array

Introduction: In this problem, you will use the suffix array to solve the Multiple Pattern Matching Problem.
    This is what actually happens when one needs to solve the pattern matching problem for a massive string
    like the human genome: instead of downloading the genome itself, one downloads its suffix array and
    solves the pattern matching problem using the array.

Task: Find all occurrences of a given collection of patterns in a string.

Input: The first line contains a string Text. The second line specifies an integer n. The last line gives a
    collection of n strings Patterns = {p_1, ..., p_n} separated by spaces.

Constraints: 1 <= |Text| <= 10^5; 1 <= n <= 10^4; SUM[i=1->n]|p_i| <= 10^5; all strings contain only the
    symbols A, C, G, T.

Output: All starting positions (in any order) in Text where a pattern appears as a substring (using 0-based
    indexing as usual). If several patterns occur at the same position in the Text, still output this
    position only once.
"""

import sys


def sort_characters(text):
    alphabet = sorted(set(text))
    order = [0 for _ in text]
    count = {i: 0 for i in alphabet}
    for i, _ in enumerate(text):
        count[text[i]] += 1
    for j in range(1, len(alphabet)):
        count[alphabet[j]] += count[alphabet[j - 1]]
    for i in range(len(text) - 1, -1, -1):
        c = text[i]
        count[c] -= 1
        order[count[c]] = i
    return order


def sort_characters_alternative(text):
    alphabet = sorted(set(text))
    order = [0 for _ in text]
    count = [text.count(char) for char in alphabet]
    for j in range(1, len(alphabet)):
        count[j] += count[j - 1]
    for i in range(len(text) - 1, -1, -1):
        c = text[i]
        count[alphabet.index(c)] -= 1
        order[count[alphabet.index(c)]] = i
    return order


def compute_char_classes(text, order):
    char_class = [0 for _ in text]
    char_class[order[0]] = 0
    for i in range(1, len(text)):
        if text[order[i]] != text[order[i - 1]]:
            char_class[order[i]] = char_class[order[i - 1]] + 1
        else:
            char_class[order[i]] = char_class[order[i - 1]]
    return char_class


def sort_doubled(text, l, order, char_class):
    count = [0 for _ in text]
    new_order = [0 for _ in text]
    for i in range(len(text)):
        count[char_class[i]] += 1
    for j in range(1, len(text)):
        count[j] += count[j - 1]
    for i in range(len(text) - 1, -1, -1):
        start = (order[i] - l + len(text)) % len(text)
        cl = char_class[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_classes(new_order, char_class, l):
    n = len(new_order)
    new_class = [0 for _ in range(n)]
    new_class[new_order[0]] = 0
    for i in range(1, n):
        curr = new_order[i]
        prev = new_order[i - 1]
        mid = curr + l
        mid_prev = (prev + l) % n
        if char_class[curr] != char_class[prev] or char_class[mid] != char_class[mid_prev]:
            new_class[curr] = new_class[prev] + 1
        else:
            new_class[curr] = new_class[prev]
    return new_class


def build_suffix_array(text):
    """
    Build the suffix array of the string text and return a list result of the same
    length as the text such that the value result[i] is the 0-based index in text
    where the i-th lexicographically smallest suffix of text starts.
    """
    order = sort_characters(text)
    char_class = compute_char_classes(text, order)
    length = 1
    while length < len(text):
        order = sort_doubled(text, length, order, char_class)
        char_class = update_classes(order, char_class, length)
        length *= 2
    return order


def find_occurrences_of_pattern(text, pattern):
    min_idx = 0
    max_idx = len(text)
    while min_idx < max_idx:
        mid_idx = (min_idx + max_idx) // 2
        if pattern > text[suffix_array[mid_idx]:]:
            min_idx = mid_idx + 1
        else:
            max_idx = mid_idx
    start = min_idx
    max_idx = len(text)
    while min_idx < max_idx:
        mid_idx = (min_idx + max_idx) // 2
        if pattern == text[suffix_array[mid_idx]:suffix_array[mid_idx] + len(pattern)]:
            min_idx = mid_idx + 1
        else:
            max_idx = mid_idx
    end = max_idx
    if start > end:
        return
    else:
        return start, end


def find_occurrences(text, patterns):
    occs = set()
    for pattern in patterns:
        start, end = find_occurrences_of_pattern(text, pattern)
        for i in range(start, end):
            occs.add(suffix_array[i])
    return occs


if __name__ == '__main__':
    text = sys.stdin.readline().strip() + '$'
    suffix_array = build_suffix_array(text)
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))
