# python3

"""
2. Compute tree height

Task: Given a description of a rooted tree, compute its height. Recall that the height of a (rooted) tree is the
    maximum depth of a node, or the maximum distance from a leaf to the root. The tree is not necessarily binary.
.
Input: The first line contains the number of nodes n. The second line contains n integers from -1 to n - 1, where
    the i-th integer corresponds to the parent of node i. If the i-th one of them (0 <= i <= n - 1) is -1, node i
    is the root. It is guaranteed that there is exactly one root, and that the input represents a tree.

Constraints: 1 <= n <= 10^5.

Output: The height of the tree.
"""

import sys, threading
from collections import deque

sys.setrecursionlimit(10**7)  # Max depth of recursion.
threading.stack_size(2**27)  # New thread will get stack of this size.


# Naive, inefficient algorithm.
def compute_height_naive(n, parent):
    max_height = 0
    for vertex in range(n):
        height = 0
        i = vertex
        while i != -1:
            height += 1
            i = parent[i]
        max_height = max(max_height, height)
    return max_height


# More efficient algorithm.
def compute_height(n, parent):
    nodes = [[] for _ in range(n)]  # Will contain child nodes of each node.
    for i, node in enumerate(parent):
        if node == -1:
            root = i
        else:
            nodes[node].append(i)
    q = deque()
    q.append((root, 1))  # Append tuple containing root node and its height.
    while q:
        node_number, node_height = q.popleft()
        for n in nodes[node_number]:
            q.append((n, node_height + 1))
    return node_height  # Deepest node will appear last in BFS.


def main():
    n = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    print(compute_height(n, parent))


threading.Thread(target=main).start()
