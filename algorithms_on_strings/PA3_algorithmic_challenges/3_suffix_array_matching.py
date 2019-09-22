# python3
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
    Build suffix array of the string text and return a list result of
    the same length as the text such that the value result[i] is the
    index (0-based) in text where the i-th lexicographically smallest
    suffix of text starts.
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
