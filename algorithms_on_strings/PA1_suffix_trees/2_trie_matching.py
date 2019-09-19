# python3
import sys

# 2. Multiple pattern matching
# Task: Find all occurrences of a collection of patterns in a text.
# Input: The first line of the input contains a string Text, the second line contains an integer n, and each of the
#     following n lines contains a pattern from Patterns = {p_1, ..., p_n}.
# Constraints: 1 <= |Text| <= 10000; 1 <= n <= 5000; 1 <= |p_i| <= 100 for all 1 <= i <= n; all strings contain only
#     symbols A, C, G, T; no p_i is a prefix of p_j for all 1 <= i != j <= n.
# Output: All starting positions in Text where a string from Patterns appears as a substring, in increasing order.


def build_trie(patterns):
    trie = dict()
    node_num = 0
    for string in patterns:
        curr_node = 0
        for i in string:
            if curr_node not in trie:
                trie[curr_node] = {}
            if i in trie[curr_node]:
                curr_node = trie[curr_node][i]
            else:
                node_num += 1
                trie[curr_node][i] = node_num
                curr_node = node_num
    return trie


def solve(text, patterns):
    result = []
    trie = build_trie(patterns)
    for i, _ in enumerate(text):
        curr_node = 0
        char_index = i
        while curr_node in trie and char_index < len(text) and text[char_index] in trie[curr_node]:
            curr_node = trie[curr_node][text[char_index]]
            char_index += 1
        if curr_node not in trie:
            result.append(i)
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
    result = solve(text, patterns)
    sys.stdout.write(' '.join(map(str, result)) + '\n')
