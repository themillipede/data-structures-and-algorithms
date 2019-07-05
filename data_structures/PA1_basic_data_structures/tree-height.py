# python3
import sys, threading
from collections import deque
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# 2. Compute tree height
# Task: Given a description of a rooted tree, compute its height.
# Input: The first line contains the number of nodes n. The second line contains n integers from -1 to n - 1, where
#     the i-th integer corresponds to the parent of node i (0 <= i <= n - 1). If the i-th one of them is -1, node i
#     is the root. It is guaranteed that there is exactly one root, and that the input represents a tree.
# Constraints: 1 <= n <= 10^5.
# Output: The height of the tree.


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


def compute_height(n, parent):
    nodes = [[] for _ in range(n)]
    for i, node in enumerate(parent):
        if node == -1:
            root = i
        else:
            nodes[node].append(i)
    q = deque()
    q.append((root, 1))
    while q:
        node = q.popleft()
        node_number = node[0]
        node_height = node[1]
        for n in nodes[node_number]:
            q.append((n, node_height + 1))
    return node_height


def main():
    n = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    print(compute_height(n, parent))


threading.Thread(target=main).start()
