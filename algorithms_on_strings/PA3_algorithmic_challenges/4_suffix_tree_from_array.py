# python3

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
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
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
