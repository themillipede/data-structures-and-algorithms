# python3

"""
3. Generalized multiple pattern matching

Task: Extend the solution for the previous problem such that it can handle cases when one of the patterns is a
    prefix of another pattern. In this case, some patterns are spelled in a trie by traversing a path from the
    root to an internal vertex rather than to a leaf.

Input: The first line contains a string Text, the second line contains an integer n, and each of the following
    n lines contains a pattern from Patterns = {p_1, ..., p_n}.

Constraints: 1 <= |Text| <= 10000; 1 <= n <= 5000; 1 <= |p_i| <= 100 for all 1 <= i <= n; all strings contain
    only symbols A, C, G, T; it can be the case that p_i is a prefix of p_j for some i, j.

Output: All starting positions in Text where a string from Patterns appears as a substring in increasing order.
    If more than one pattern appears starting at position i, output i once.
"""

import sys


def build_trie(patterns):
    """
    If we sort the patterns alphabetically, then any pattern that is a prefix of another pattern will come before
    the other pattern in the ordering. Since we only need to output the set of distinct starting positions in the
    text of any matching patterns, and not the specific patterns that match at those positions, we can remove any
    pattern for which another pattern is a prefix. The output of this function is thus a reduced trie containing
    only patterns that do not have any other pattern as a prefix.
    """
    patterns.sort()
    trie = dict()
    leaves = set()
    node_num = 0
    for string in patterns:
        curr_node = 0
        for idx, i in enumerate(string):
            if curr_node not in trie:
                trie[curr_node] = {}
            if i in trie[curr_node]:
                curr_node = trie[curr_node][i]
            else:
                node_num += 1
                trie[curr_node][i] = node_num
                curr_node = node_num
            if curr_node in leaves:
                break
            if idx == len(string) - 1:
                leaves.add(curr_node)
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
