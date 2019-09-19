# python3
import sys

# 2. Determining an order of courses
# Task: Compute a topological ordering of a given directed acyclic graph (DAG).
# Input: A directed graph with n vertices and m edges.
# Constraints: 1 <= n <= 10^5, 0 <= m <= 10^5. The given graph is guaranteed to be acyclic.
# Output: Any topological ordering of the vertices.


def dfs(adj, used, order, node):
    used[node] = 1
    for n in adj[node]:
        if not used[n]:
            dfs(adj, used, order, n)
    order.append(node)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for node, _ in enumerate(adj):
        if not used[node]:
            dfs(adj, used, order, node)
    order.reverse()
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
