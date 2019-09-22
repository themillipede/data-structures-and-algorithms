# python3

"""
Advanced Problem: Construct the suffix tree from the suffix array

Introduction: As we've mentioned earlier, known algorithms for constructing suffix trees in linear time are
    quite complex. It turns out, however, that one can first construct a suffix array in near-linear time
    (say, O(nlogn)) and then transform it into a suffix tree in linear time. This gives a near-linear time
    algorithm for constructing a suffix tree!

    SuffixTree(Text) can be constructed in linear time from SuffixArray(Tree) by using the longest common prefix
    (LCP) array of Text, LCP(Text), which stores the length of the longest common prefix shared by consecutively
    lexicographically ordered suffixes of Text.
    For example, LCP("panamabananas$") = (0, 1, 1, 3, 3, 1, 0, 0, 0, 2, 2, 0, 0).

Task: Construct a suffix tree from the suffix array and LCP array of a string.

Input: The first line contains a string Text ending with a "$" symbol. The second line contains SuffixArray(Text)
    as a list of |Text| integers separated by spaces. The last line contains LCP(Text) as a list of |Text| - 1
    integers separated by spaces.

Constraints: 1 <= |Text(Text)| <= 2*10^5; except for the last symbol, Text contains only the symbols A, C, G, T.

Output: The output format in this problem differs from the output format in the problem "Suffix Tree" from PA2 and
    is somewhat tricky. It is because this problem is harder: the input string can be longer, so it would take too
    long to output all the edge labels directly and compare them with the correct ones, as their combined length
    can be Theta(|Text|^2), which is too much when the Text can be as long as 200000 characters.

    Output the Text from the input on the first line. Then output all the edges of the suffix tree in a specific
    order (see below), each on its own line. Output each edge as a pair of integers (start, end), where start is
    the position in the Text corresponding to the start of the edge label substring in the Text and end is the
    position right after the end of the edge label in the Text. Note that start must be a valid position in the
    Text, that is, 0 <= start <= |Text| - 1, and 1 <= end <= |Text|. Substring Text[start..end - 1] must be equal
    to the edge label of the corresponding edge. For example, if Text = "ACACAA$" and the edge label is "CA", you
    can output this edge either as (1, 3) corresponding to Text[1..2] = "CA" or as (3, 5) corresponding to
    Text[3..4] = "CA" -- both variants will be accepted.

    The order of the edges is important here -- if you output all the correct edges in the wrong order, your
    solution will not be accepted. Output all the edges in the order of sorted suffixes: first, take the leaf of
    the suffix tree corresponding to the smallest suffix of Text and output all the edges ont he path from the
    root to this leaf. Then take the leaf corresponding to the second smallest suffix of Text and output all the
    edges on the path from the root to this leaf except for those edges which were printed before. Then take the
    leaf corresponding to the third smallest suffix, fourth smallest suffix and so on. Print each edge only once
    -- as a part of the path corresponding to the smallest suffic of Text where this edge appears. This way, you
    will only output O(|Text|) integers.
"""

import sys


class Node:
    def __init__(self, parent, string_depth, edge_start, edge_end):
        self.children = {}
        self.parent = parent
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end
        self.id = None


def create_new_leaf(node, text, suffix_idx):
    leaf = Node(
        parent=node,
        string_depth=len(text) - suffix_idx,
        edge_start=suffix_idx + node.string_depth,
        edge_end=len(text) - 1
    )
    node.children[text[leaf.edge_start]] = leaf
    return leaf


def break_edge(node, text, start, offset):
    start_char = text[start]
    mid_char = text[start + offset]
    mid_node = Node(node, node.string_depth + offset, start, start + offset - 1)
    mid_node.children[mid_char] = node.children[start_char]
    node.children[start_char].parent = mid_node
    node.children[start_char].edge_start += offset
    node.children[start_char] = mid_node
    return mid_node


def suffix_array_to_suffix_tree(suffix_array, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array and LCP array
    lcp_array. Return the tree as a mapping from a node ID to the list of all outgoing
    edges of the corresponding node. The edges in the list must be sorted in the ascending
    order by the first character of the edge label. Root must have node ID = 0, and all
    other node IDs must be different nonnegative integers. Each edge must be represented
    by a tuple (node, start, end), where
        - node is the node ID of the ending node of the edge
        - start is the starting position (0-based) of the substring of text corresponding to the edge label
        - end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from the root to a node with
    ID 1 must be represented by a tuple (1, 6, 7). This edge must be present in the list
    tree[0] (corresponding to the root node), and it should be the first edge in the list
    (because it has the smallest first character of all edges outgoing from the root).
    """
    root = Node(parent=None, string_depth=0, edge_start=-1, edge_end=-1)
    id = 0
    root.id = id
    tree = [root]
    lcp_prev = 0
    cur_node = root
    for i, _ in enumerate(text):
        suffix_idx = suffix_array[i]
        while cur_node.string_depth > lcp_prev:
            cur_node = cur_node.parent
        if cur_node.string_depth == lcp_prev:
            cur_node = create_new_leaf(cur_node, text, suffix_idx)
            id += 1
            cur_node.id = id
        else:
            edge_start = suffix_array[i - 1] + cur_node.string_depth
            offset = lcp_prev - cur_node.string_depth
            mid_node = break_edge(cur_node, text, edge_start, offset)
            id += 1
            mid_node.id = id
            tree.append(mid_node)
            cur_node = create_new_leaf(mid_node, text, suffix_idx)
            id += 1
            cur_node.id = id
        if i < len(text) - 1:
            lcp_prev = lcp[i]
    suffix_tree = {}
    for node in tree:
        edge_list = sorted([(k, v.id, v.edge_start, v.edge_end + 1) for k, v in node.children.items()])
        suffix_tree[node.id] = [item[1:] for item in edge_list]
    return suffix_tree


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    tree = suffix_array_to_suffix_tree(sa, lcp, text)

    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
        node, edge_index = stack.pop()
        if not node in tree:
            continue
        edges = tree[node]
        if edge_index + 1 < len(edges):
            stack.append((node, edge_index + 1))
        print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
        stack.append((edges[edge_index][0], 0))
