# python3
import sys

# 1. Finding an exit from a maze
# Task: Given an undirected graph and two distinct vertices u and v, check if there is a path between u and v.
# Input: An undirected graph with n vertices and m edges. The next line contains two of the vertices, u and v.
# Constraints: 2 <= n <= 10^3; 1 <= m <= 10^3; 1 <= u, v <= n; u != v.
# Output: 1 if there is a path between u and v and 0 otherwise.


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
