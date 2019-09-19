# python3

"""
1. Finding an exit from a maze

Introduction: A maze is a rectangular grid of cells with walls between some of adjacent cells. You would like to
    check whether there is a path from a given cell to a given exit in a maze, where an exit is also a cell that
    lies on the border of the maze. For this, you can represent the maze as an undirected graph: vertices of the
    graph are cells of the maze; two vertices are connected by an undirected edge if they are adjacent and there
    is no wall between them. Then, to check whether there is a path between two given cells in the maze, it
    suffices to check that there is a path between the corresponding two vertices in the graph.

Task: Given an undirected graph and two distinct vertices u and v, check if there is a path between u and v.

Input: The first line contains the number of vertices and edges, n and m, respectively. Each of the following m
    lines contains two of the vertices, u and v, defining an edge between u and v. Vertices are numbered 1 to n.

Constraints: 2 <= n <= 10^3; 1 <= m <= 10^3; 1 <= u, v <= n; u != v. It is guaranteed that the given graph is
    simple. That is, it does not contain self-loops or parallel edges.

Output: 1 if there is a path between u and v and 0 otherwise.
"""

import sys


def explore(x, y, visited, adj):
    visited.add(x)
    if x == y:
        return True
    for w in adj[x]:
        if w not in visited:
            if explore(w, y, visited, adj):
                return True
    return False


def reach(adj, u, v):
    visited = set()
    if explore(u, v, visited, adj):
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
        adj[b - 1].append(a - 1)
    u, v = data[2 * m:]
    u, v = u - 1, v - 1
    print(reach(adj, u, v))
