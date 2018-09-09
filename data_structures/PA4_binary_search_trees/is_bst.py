#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):

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
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
