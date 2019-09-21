# python3

"""
2. Plan a fun party

Introduction: In this problem, you will design and implement an efficient algorithm to invite the coolest people
    from your company to a party in such a way that everybody is relaxed, because the direct boss of any invited
    person is not invited.

Task: You're planning a company party. You'd like to invite the coolest people, and you've assigned each one of
    them a fun factor -- the greater the fun factor, the cooler the person is. You want to maximize the total
    fun factor (sum of the fun factors of all the invited people). However, you can't invite everyone, because
    if the direct boss of some invited person is also invited, it will be awkward. Find out what is the maximum
    possible total fun factor.

Input: The first line contains an integer n -- the number of people in the company. The next line contains n
    numbers f_i -- the fun factors of each of the n people in the company. Each of the next n - 1 lines describes
    the subordination structure. Everyone but for the CEO of the company has exactly one direct boss. There are
    no cycles: nobody can be a boss of a boss of a ... of a boss of himself. So, the subordination structure is a
    regular tree. Each of the n - 1 lines contains two integers u and v, and you know that either u is the boss of
    v or vice versa (you don't really need to know which one is the boss, but you can invite only one of them or
    none of them).

Constraints: 1 <= n <= 100000; 1 <= f_i <= 1000; 1 <= u, v <= n; u != v.

Output: The maximum possible total fun factor of the party (the sum of fun factors of all the invited people).
"""

import sys
import threading

from collections import deque

# This code is used to avoid stack overflow issues.
sys.setrecursionlimit(10**6)  # Max depth of recursion.
threading.stack_size(2**26)  # New thread will get stack of this size.


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.parent = None


def bfs(tree, vertex):
    """
    The input tree treats any neighbour of a vertex as a child of that vertex (so if u is connected to v,
    then v will be listed as a child of u AND u will be listed as a child of v). This function derives a
    subordination structure for the tree, with consistent one-way parent-child relationships throughout.
    """
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
        # Keep track of the maximum independent set weight
        # for the subtree rooted at each node of the tree.
        memo = [float('inf') for _ in range(len(tree))]
    if memo[vertex] == float('inf'):
        if not tree[vertex].children:
            memo[vertex] = tree[vertex].weight  # Leaf vertex, so maximum subtree weight is vertex weight.
        else:
            m1 = tree[vertex].weight
            for u in tree[vertex].children:
                for w in tree[u].children:  # Add maximum subtree weights of grandchildren but not children.
                    m1 += fun_party(tree, w, memo)  # Maximum subtree weight at vertex including vertex weight.
            m0 = 0
            for u in tree[vertex].children:  # Add maximum subtree weights of children but not grandchildren.
                m0 += fun_party(tree, u, memo)  # Maximum subtree weight at vertex excluding vertex weight.
            memo[vertex] = max(m1, m0)
    return memo[vertex]


def max_weight_independent_tree_subset(tree):
    size = len(tree)
    if size == 0:
        return 0
    tree = bfs(tree, 0)
    return fun_party(tree, 0, memo=None)


def main():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    weight = max_weight_independent_tree_subset(tree)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
