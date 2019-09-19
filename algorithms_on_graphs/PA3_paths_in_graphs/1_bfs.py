# python3

"""
2. Computing the minimum number of flight segments

Introduction: You would like to compute the minimum number of flight segments to get from one city to another.
    For this, you construct the following undirected graph: vertices represent cities, and there is an edge
    between two vertices whenever there is a flight between the corresponding two cities. Then, it suffices to
    find a shortest path from one of the given cities to the other one.

Task: Given an undirected graph with n vertices and m edges and two vertices u and v, compute the length of a
    shortest path between u and v (that is, the minimum number of edges in a path from u to v).

Input: An undirected graph is given in the standard format. The next line contains the two vertices u and v.

Constraints: 2 <= n <= 10^5; 0 <= m <= 10^5; u != v; 1 <= u, v <= n.

Output: The minimum number of edges in a path from u to v, or -1 if there is no path.
"""

import sys
import queue


def distance(adj, s, t):
    visited = [0] * len(adj)
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        n = q.get()
        num_edges = visited[n] + 1
        for node in adj[n]:
            if node == t:
                return num_edges
            if not visited[node]:
                visited[node] = num_edges
                q.put(node)
    return -1


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
