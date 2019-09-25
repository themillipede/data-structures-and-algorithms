#!/usr/bin/python3

"""
2. Is it a binary search tree?

Task: You are given a binary tree with integers as its keys. You need to test whether it is a binary search tree.
    The definition of a binary search tree is the following: for any node of the tree with key x, the key of any
    node in its left subtree must be strictly less than x, and the key of any node in its right subtree must be
    strictly greater than x. You are guaranteed that the input contains a valid binary tree.

Input: The first line contains the number of vertices n. The vertices of the tree are numbered from 0 to n - 1.
    Vertex 0 is the root. The next n lines contain information about vertices 0, 1, ..., n - 1 in order. Each of
    these lines contains three integers key_i, left_i and right_i -- key_i is the key of the i-th vertex, left_i
    is the index of the left child of the i-th vertex, and right_i is the index of the right child of the i-th
    vertex. If i doesn't have a left or right child, the corresponding left_i or right_i will be equal to -1.

Constraints: 1 <= n <= 10^5; -2^31 <= key_i <= 2^31 - 1; -1 <= left_i, right_i <= n - 1. It is guaranteed that the
    input represents a valid binary tree. In particular, if left_i != -1 and right_i != -1, then left_i != right_i.
    Also, a vertex cannot be a child of two different vertices, and each vertex is a descendant of the root vertex.
    All keys in the input will be different.

Output: If the given binary tree is a binary search tree, output "CORRECT". Otherwise output "INCORRECT".
"""

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def is_binary_search_tree_unique(tree):
    """
    Checks whether the input binary tree is a binary search tree.
    All the node values must be unique for this function to work.

    Conducts in-order traversal of the tree starting at the root,
    and checks whether the resulting sequence is in sorted order.
    """
    if not tree:
        return True

    def in_order(tree):
        result = []

        def in_order_traversal(root):
            if root[1] != -1:
                in_order_traversal(tree[root[1]])
            result.append(root[0])
            if root[2] != -1:
                in_order_traversal(tree[root[2]])

        in_order_traversal(tree[0])
        return result

    traversal = in_order(tree)
    return traversal == sorted(traversal)


def is_binary_search_tree(tree):

    max_lower = float('-inf')
    min_higher = float('inf')

    def is_bst(tree, n, max_lower, min_higher):
        if n == -1 or not tree:
            return True
        if tree[n][0] < max_lower or tree[n][0] > min_higher:
            return False
        if not is_bst(tree, tree[n][1], max_lower, tree[n][0]):
            return False
        if not is_bst(tree, tree[n][2], tree[n][0], min_higher):
            return False
        return True

    return is_bst(tree, 0, max_lower, min_higher)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if is_binary_search_tree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
