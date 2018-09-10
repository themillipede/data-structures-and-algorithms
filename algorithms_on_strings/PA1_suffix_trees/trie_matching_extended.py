# python3
import sys

NA = -1


class Node:
    def __init__(self):
        self.next = [NA] * 4
        self.patternEnd = False


def build_trie(patterns):
    tree = dict()
    node_num = 0
    for string in patterns:
        curr_node = 0
        for i, char in enumerate(string):
            if curr_node not in tree:
                tree[curr_node] = {}
            if char in tree[curr_node]:
                if i == len(string) - 1:
                    tree[curr_node][char][1] = 1
                curr_node = tree[curr_node][char][0]
            else:
                node_num += 1
                if i == len(string) - 1:
                    tree[curr_node][char] = [node_num, 1]
                else:
                    tree[curr_node][char] = [node_num, 0]
                curr_node = node_num
    return tree


def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    for i, _ in enumerate(text):
        curr_node = 0
        char_index = i
        is_end = 0
        while curr_node in trie and char_index < len(text) and text[char_index] in trie[curr_node]:
            is_end = trie[curr_node][text[char_index]][1]
            curr_node = trie[curr_node][text[char_index]][0]
            char_index += 1
        if curr_node not in trie or is_end == 1:
            result.append(i)
    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
