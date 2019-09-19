# python3

"""
3. Advanced Problem: Checking whether any intersection in a city is reachable from any other

Introduction: The police department of a city has made all streets one-way. You would like to check whether it is
    still possible to drive legally from any intersection to any other intersection. For this, you construct a
    directed graph: vertices are intersections, and there is an edge (u, v) for each (one-way) street from u to v.
    Then, it suffices to check whether all the vertices in the graph lie in the same strongly connected component.

Task: Compute the number of strongly connected components in a given directed graph with n vertices and m edges.

Input: A directed graph is given in the standard format.

Constraints: 1 <= n <= 10^4, 0 <= m <= 10^4.

Output: The number of strongly connected components.
"""

import sys

sys.setrecursionlimit(200000)


def dfs_order(node, visited, adj, stack):
    visited[node] = 1
    for n in adj[node]:
        if not visited[n]:
            dfs_order(n, visited, adj, stack)
    stack.append(node)


def transpose_adjacency_list(adj):
    transpose = [[] for _ in range(len(adj))]
    for i, nodes in enumerate(adj):
        for n in nodes:
            transpose[n].append(i)
    return transpose


def dfs(node, visited, adj):
    visited[node] = 1
    for n in adj[node]:
        if not visited[n]:
            dfs(n, visited, adj)


def number_of_strongly_connected_components(adj):
    result = 0
    stack = []
    visited = [0] * len(adj)
    for n, _ in enumerate(adj):
        if not visited[n]:
            dfs_order(n, visited, stack, adj)
    transpose = transpose_adjacency_list(adj)
    visited = [0] * len(adj)
    while stack:
        n = stack.pop()
        if not visited[n]:
            result += 1
            dfs(n, visited, transpose)
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
    print(number_of_strongly_connected_components(adj))
