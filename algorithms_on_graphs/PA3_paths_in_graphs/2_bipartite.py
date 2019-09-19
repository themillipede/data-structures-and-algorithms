# python3

"""
2. Checking whether a graph is bipartite

Introduction: An undirected graph is called "bipartite" if its vertices can be split into two parts such that each
    edge of the graph joins two vertices from different parts. Bipartite graphs arise naturally in applications
    where a graph is used to model connections between objects of two different types (for example, boys and girls,
    or students and dormitories). An alternative definition is the following: a graph is bipartite if its vertices
    can be coloured with two different colours such that the endpoints of each edge have different colours.

Task: Given an undirected graph with n vertices and m edges, check whether it is bipartite.

Input: An undirected graph is given in the standard format.

Constraints: 1 <= n <= 10^5; 0 <= m <= 10^5.

Output: 1 if the graph is bipartite and 0 otherwise.
"""

import sys
import queue


def bipartite(adj):
    q = queue.Queue()
    label = [0] * len(adj)
    if not adj:
        return -1
    label[0] = 1
    q.put(0)
    while not q.empty():
        node = q.get()
        for n in adj[node]:
            if label[n] == label[node]:
                return 0
            if not label[n]:
                label[n] = 2 if label[node] == 1 else 1
                q.put(n)
    return 1


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
    print(bipartite(adj))
