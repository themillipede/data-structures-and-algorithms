# python3
import sys

# 1. Checking consistency of CS curriculum
# Task: Check whether a given directed graph contains a cycle.
# Input: A directed graph with n vertices and m edges.
# Constraints: 1 <= n <= 10^3, 0 <= m <= 10^3.
# Output: 1 if the graph contains a cycle and 0 otherwise.


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
