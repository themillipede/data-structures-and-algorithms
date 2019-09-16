# python3
import sys

# 1. Construct a trie from a collection of patterns
# Task: Construct a trie from a collection of patterns.
# Input: An integer n and a collection of strings, Patterns = {p_1, ..., p_n} (with each string on a separate line).
# Constraints: 1 <= n <= 100; 1 <= |p_i| <= 100 for all 1 <= i <= n; p_i's contain only symbols A, C, G, T; no p_i
#     is a prefix of p_j for all 1 <= i != j <= n.
# Output: The adjacency list for Trie(Patterns), in the following format: if Trie(Patterns) has n nodes, first label
#     the root with 0 and then label the remaining nodes with the integers 1 to n - 1 in any order. Each edge of the
#     adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the
#     integers i, j labelling the initial and terminal nodes of the edge, respectively, and the third member of the
#     triple must be the symbol c labelling the edge. Output each such triple in the format u->v:c (with no spaces)
#     on a separate line.
# The trie built from patterns should take the form of a dictionary of dictionaries, where the keys of the external
# dictionary are node IDs, and the internal dictionaries contain all the trie edges outgoing from the corresponding
# node. The keys are the letters on those edges, and the values are the IDs of the nodes to which those edges lead.


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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    trie = build_trie(patterns)
    for node in trie:
        for c in trie[node]:
            print("{}->{}:{}".format(node, trie[node][c], c))
