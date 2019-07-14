# python3
import sys

# 4. Construct the suffix tree of a string
# Task: Construct the suffix tree of a string.
# Input: A string Text ending witha "$" symbol.
# Constraints: 1 <= |Text| <= 5000; except for the last symbol, Text contains symbols A, C, G, T only.
# Output: The strings labelling the edges of the suffix tree in any order.


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
    newest_node = 0
    for suffix_start_idx, _ in enumerate(text):
        newest_node = incorporate_latest_substring(text, suffix_start_idx, tree, newest_node)
    return tree


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    suffix_tree = build_suffix_tree(text)
    result = []
    for node, edges in suffix_tree.items():
        for edge in edges:
            start = edge[0]
            length = edge[1]
            result.append(text[start:start + length])
    print("\n".join(result))
