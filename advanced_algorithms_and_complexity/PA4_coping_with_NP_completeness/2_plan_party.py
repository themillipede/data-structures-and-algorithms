# python3
import sys
import threading

from collections import deque

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.parent = None


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def bfs(tree, vertex):
    new_tree = [Vertex(v.weight) for v in tree]
    q = deque()
    q.append(vertex)
    while q:
        v = q.popleft()
        for child in tree[v].children:
            tree[child].parent = v
            if child != tree[v].parent:
                new_tree[v].children.append(child)
                q.append(child)
    return new_tree


def fun_party(tree, vertex, memo=None):
    if not memo:
        memo = [float('inf') for _ in range(len(tree))]
    if memo[vertex] == float('inf'):
        if not tree[vertex].children:
            memo[vertex] = tree[vertex].weight
        else:
            m1 = tree[vertex].weight
            for u in tree[vertex].children:
                for w in tree[u].children:
                    m1 += fun_party(tree, w, memo)
            m0 = 0
            for u in tree[vertex].children:
                m0 += fun_party(tree, u, memo)
            memo[vertex] = max(m1, m0)
    return memo[vertex]


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    tree = bfs(tree, 0)
    return fun_party(tree, 0, memo=None)


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
