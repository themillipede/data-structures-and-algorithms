# python3
import sys


def build_tree(text):
    tree = dict()
    node_num = 0
    for suffix_start_index, _ in enumerate(text):
        curr_node = 0
        j = suffix_start_index
        while j < len(text):
            if curr_node not in tree:
                tree[curr_node] = {}
            letter_to_edge = {text[edge[0]]: edge for edge in tree[curr_node]}
            if text[j] in letter_to_edge:
                suffix_start = letter_to_edge[text[j]][0]
                suffix_length = letter_to_edge[text[j]][1]
                k = suffix_start
                l = 0
                while text[j] == text[k] and l < suffix_length:
                    j += 1
                    k += 1
                    l += 1
                if l == suffix_length:
                    curr_node = tree[curr_node][(suffix_start, suffix_length)]
                else:
                    node_to_split = tree[curr_node][(suffix_start, suffix_length)]
                    tree[curr_node][(suffix_start, l)] = node_to_split
                    if node_to_split not in tree:
                        tree[node_to_split] = {}
                    node_num += 1
                    tree[node_to_split][(k, suffix_length - l)] = node_num
                    node_num += 1
                    tree[node_to_split][(j, len(text) - j)] = node_num
                    del tree[curr_node][(suffix_start, letter_to_edge[text[suffix_start]][1])]
                    curr_node = node_num
                    j += suffix_length - (k + l)
            else:
                node_num += 1
                tree[curr_node][(j, len(text) - j)] = node_num
                j = len(text)
    return tree


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    result = []
    suffix_tree = build_tree(text)
    print(suffix_tree)
    for node, edges in suffix_tree.items():
        for edge in edges:
            start = edge[0]
            length = edge[1]
            result.append((text[start:start + length], start))
    return result
print(build_suffix_tree('ATAAATG$'))
'''
if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
'''
