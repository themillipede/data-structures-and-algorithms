# python3
import sys

# 2. Adding exits to a maze
# Task: Given an undirected graph, compute the number of connected components.
# Input: An undirected graph with n vertices and m edges.
# Constraints: 1 <= n <= 10^3, 0 <= m <= 10^3.
# Output: The number of connected components.


def explore(node, visited, adj):
    visited.add(node)
    for n in adj[node]:
        if n not in visited:
            explore(n, visited, adj)


def number_of_components(adj):
    result = 0
    visited = set()
    for node, _ in enumerate(adj):
        if node not in visited:
            explore(node, visited, adj)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))