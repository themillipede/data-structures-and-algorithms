# python3

"""
4. Construct the suffix tree of a string

Introduction: A suffix tree is an extremely powerful indexing data structure having applications in areas like
    pattern matching, data compression, and bioinformatics. The goal in this problem is to implement this data
    structure. Storing Trie(Patterns) requires a great deal of memory, so we should process Text into a data
    structure instead. Our goal is to compare each string in Patterns against Text without needing to traverse
    Text from beginning to end.

    A suffix trie, denoted SuffixTrie(Text), is the trie formed from all suffixes of Text. From now on, we will
    append the dollar sign ("$") to Text in order to mark the end of Text. We will also label each leaf of the
    resulting trie by the starting position of the suffix whose path through the trie ends at that leaf (using
    0-based indexing). This way, when we arrive at a leaf, we will immediately know where this suffix came from
    in Text. However, the runtime and memory required to construct SuffixTrie(Text) are equal to the combined
    length of all suffixes in Text. Thus, we need to reduce both the construction time and memory requirements
    of suffix tries to make them practical.

    We can reduce the number of edges in SuffixTrie(Text) by combining the edges on any non-branching path into
    a single edge. We can then label this edge with the concatenation of symbols on the consolidated edges. The
    resulting data structure is called a suffix tree, written SuffixTree(Text). To match a single Pattern to
    Text, we thread Pattern into SuffixTree(Text) by the same process used for a suffix trie. Similarly to the
    suffix trie, we can use the leaf labels to find starting positions of successfully matched patterns.

    Suffix trees save memory because they do not need to store concatenated edge labels from each non-branching
    path. For example, a suffix tree does not need ten bytes to store the edge labeled "mabananas$" in
    SuffixTree("panamabananas$"); instead, it suffices to store a pointer to position 4 of "panamabananas$", as
    well as the length of "mabananas$". Furthermore, suffix trees can be constructed in linear time, without
    having to first construct the suffix trie! We won't ask you to implement this fast suffix tree construction
    algorithm because it is quite complex.

Task: Construct the suffix tree of a string.

Input: A string Text ending with a "$" symbol.

Constraints: 1 <= |Text| <= 5000; except for the last symbol, Text contains symbols A, C, G, T only.

Output: The strings labelling the edges of the suffix tree in any order.
"""

import sys


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
