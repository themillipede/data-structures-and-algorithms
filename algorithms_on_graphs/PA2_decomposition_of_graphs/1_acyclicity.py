# python3

"""
1. Checking consistency of CS curriculum

Introduction: A Computer Science curriculum specifies the prerequisites for each course as a list of other courses
    that should be taken before taking the course. You would like to perform a consistency check of the curriculum,
    that is, to check that there are no cyclic dependencies. For this, you construct the following directed graph:
    vertices correspond to courses; there is a directed edge (u, v) if course u should be taken before course v.
    Then, it is enough to check whether the resulting graph contains a cycle.

Task: Check whether a given directed graph with n vertices and m edges contains a cycle.

Input: The first line contains the number of vertices and edges, n and m, respectively. Each of the following m
    lines contains two of the vertices, u and v, defining a directed edge u -> v. Vertices are numbered 1 to n.

Constraints: 1 <= n <= 10^3, 0 <= m <= 10^3.

Output: 1 if the graph contains a cycle and 0 otherwise.
"""

import sys


def contains_cycle(node, visited, stack, adj):
    visited.add(node)
    stack.add(node)
    for n in adj[node]:
        if n in stack:
            return True
        if contains_cycle(n, visited, stack, adj):
            return True
    stack.remove(node)


def acyclic(adj):
    visited = set()
    stack = set()
    for node, _ in enumerate(adj):
        if node not in visited:
            if contains_cycle(node, visited, stack, adj):
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
