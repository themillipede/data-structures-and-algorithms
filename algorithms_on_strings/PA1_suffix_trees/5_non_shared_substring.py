# python3
import sys
sys.setrecursionlimit(200000)

# 5. Advanced Problem: Find the shortest non-shared substring of two strings.
# Task: Find the shortest substring of one string that does not appear in another string.#
# Input: Strings Text_1 and Text_2.
# Constraints: 1 <= |Text_1|, |Text_2| <= 2000; strings have equal length (|Text_1| = |Text_2|), are not equal
#     (Text_1 != Text_2), and contain symbols A, C, G, T only.
# Output: The shortest (non-empty) substring of Text_1 that does not appear in Text_2. (Multiple solutions may
#     exist, in which case you may return any one.)


def incorporate_latest_substring(text, suffix_start_idx, tree, newest_node):
    last_added_node = newest_node
    j = suffix_start_idx
    node = 0
    while j < len(text):
        if node not in tree:
            tree[node] = {}
        first_letter_of_edge = {text[edge[0]]: edge for edge in tree[node]}
        letter = text[j]
        if letter in first_letter_of_edge:
            relevant_edge = first_letter_of_edge[letter]
            edge_idx = relevant_edge[0]
            edge_length = relevant_edge[1]
            dest_node = tree[node][relevant_edge]
            i = edge_idx
            l = 0
            start_idx = i
            while text[i] == text[j] and l < edge_length:
                i += 1
                j += 1
                l += 1
            if text[i] != text[j] and l < edge_length:
                first_new_node = last_added_node + 1
                second_new_node = first_new_node + 1
                first_edge = (start_idx, i - start_idx)
                second_edge = (i, edge_length - first_edge[1])
                tree[node][first_edge] = first_new_node
                tree[first_new_node] = {second_edge: dest_node}
                tree[first_new_node][j, len(text) - j] = second_new_node
                del tree[node][relevant_edge]
                last_added_node = second_new_node
                j = len(text)
            elif l >= edge_length:
                node = dest_node
        else:
            last_added_node += 1
            tree[node][(j, len(text) - j)] = last_added_node
            j = len(text)
    return last_added_node


def build_suffix_tree(text):
    tree = dict()
    suffix_indices = {}
    newest_node = 0
    for suffix_start_idx, _ in enumerate(text):
        newest_node = incorporate_latest_substring(text, suffix_start_idx, tree, newest_node)
        suffix_indices[newest_node] = suffix_start_idx
    return tree, suffix_indices


# Find the shortest substring of one string that does not appear in another string.
# A "candidate" substring is either of the following:
# - The substring ending at the first character of any leaf edge containing '#' at index 1 or greater.
# - The substring ending at any node all of whose descendant leaf edges contain the '#' character.


def dfs(tree, root, suffix_indices, hash_idx, candidates=None, nonleaf_candidates=None):
    if candidates is None:
        candidates = []
    if nonleaf_candidates is None:
        nonleaf_candidates = {n: True for n in tree}
    for edge, node in tree[root].items():
        if node not in tree:  # node is a leaf
            edge_idx = edge[0]
            if edge_idx <= hash_idx:  # edge contains the hash character
                start_idx = suffix_indices[node]  # start index of suffix ending at node
                if edge_idx == hash_idx:
                    continue
                candidates.append((start_idx, edge_idx + 1))
            else:
                nonleaf_candidates[root] = False
        else:  # node is not a leaf
            dfs(tree, node, suffix_indices, hash_idx, candidates, nonleaf_candidates)
            if not nonleaf_candidates[node]:
                nonleaf_candidates[root] = False
    return candidates, nonleaf_candidates


def search(end_idx, node, tree, suffix_indices, start_indices=None):
    if not start_indices:
        start_indices = []
    if node in suffix_indices:
        start_indices.append((suffix_indices[node], end_idx))
    else:
        for _, n in tree[node].items():
            search(end_idx, n, tree, suffix_indices, start_indices)
    return start_indices


def solve(p, q):
    text = p + '#' + q + '$'
    tree, suffix_indices = build_suffix_tree(text)
    hash_idx = len(p)
    candidates, nonleaf_candidates = dfs(tree, 0, suffix_indices, hash_idx)
    for node, status in nonleaf_candidates.items():
        if status:
            for edge, n in tree[node].items():
                candidates += search(edge[0], n, tree, suffix_indices)
    shortest_substring = min(range(len(candidates)), key=lambda x: candidates[x][1] - candidates[x][0])
    result = text[candidates[shortest_substring][0]:candidates[shortest_substring][1]]
    return result


if __name__ == '__main__':
    p = sys.stdin.readline().strip()
    q = sys.stdin.readline().strip()
    result = solve(p, q)
    sys.stdout.write(result + '\n')
