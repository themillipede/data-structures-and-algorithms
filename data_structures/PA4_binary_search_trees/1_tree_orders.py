# python3

"""
1. Binary tree traversals

Task: You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.

Input: The first line contains the number of vertices n. The vertices of the tree are numbered from 0 to n - 1.
    Vertex 0 is the root. The next n lines contain information about vertices 0, 1, ..., n - 1 in order. Each of
    these lines contains three integers key_i, left_i and right_i -- key_i is the key of the i-th vertex, left_i
    is the index of the left child of the i-th vertex, and right_i is the index of the right child of the i-th
    vertex. If i doesn't have a left or right child (or either), the corresponding left_i or right_i (or both)
    will be equal to -1.

Constraints: 1 <= n <= 10^5; 0 <= key_i <= 10^9; -1 <= left_i, right_i <= n - 1. It is guaranteed that the
    input represents a valid binary tree. In particular, if left_i != -1 and right_i != -1, then left_i != right_i.
    Also, a vertex cannot be a child of two different vertices, and each vertex is a descendant of the root vertex.

Output: Print out three lines: the first line should contain the keys of the vertices in the in-order traversal
    of the tree, the second line should contain the keys of the vertices in the pre-order traversal of the tree,
    and the third line should contain the keys of the vertices in the post-order traversal of the tree.
"""

import sys, threading

sys.setrecursionlimit(10**6)  # Max depth of recursion.
threading.stack_size(2**27)  # New thread will get stack of this size.


class Tree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def in_order(self):
        result = []

        def in_order_traversal(root_index):
            if self.left[root_index] != -1:
                in_order_traversal(self.left[root_index])
            result.append(self.key[root_index])
            if self.right[root_index] != -1:
                in_order_traversal(self.right[root_index])

        in_order_traversal(0)
        return result

    def pre_order(self):
        result = []

        def pre_order_traversal(root_index):
            result.append(self.key[root_index])
            if self.left[root_index] != -1:
                pre_order_traversal(self.left[root_index])
            if self.right[root_index] != -1:
                pre_order_traversal(self.right[root_index])

        pre_order_traversal(0)
        return result

    def post_order(self):
        result = []

        def post_order_traversal(root_index):
            if self.left[root_index] != -1:
                post_order_traversal(self.left[root_index])
            if self.right[root_index] != -1:
                post_order_traversal(self.right[root_index])
            result.append(self.key[root_index])

        post_order_traversal(0)
        return result


def main():
    n = int(sys.stdin.readline())
    key = [0 for i in range(n)]
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    for i in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        key[i] = a
        left[i] = b
        right[i] = c
    tree = Tree(key, left, right)
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))

threading.Thread(target=main).start()
