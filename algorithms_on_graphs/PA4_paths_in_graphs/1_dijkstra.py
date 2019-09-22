# python3

"""
1. Computing the minimum cost of a flight

Introduction: Now, you are interested in minimizing not the number of segments, but the total cost of a flight.
    For this you construct a weighted graph: the weight of an edge from one city to another one is the cost of
    the corresponding flight.

Task: Given a directed graph with positive edge weights and with n vertices and m edges as well as two vertices
    u and v, compute the weight of a shortest path between u and v (that is, the minimum total weight of a path
    from u to v).

Input: A directed graph is given in the standard format. The next line contains the two vertices u and v.

Constraints: 1 <= n <= 10^3; 0 <= m <= 10^5; u != v; 1 <= u, v <= n; edge weights are non-negative integers not
    exceeding 10^3.

Output: The minimum weight of a path from u to v, or -1 is there is no path.
"""

import sys
import queue


def distance(adj, cost, s, t):
    dist = [float('inf') for _ in adj]
    dist[s] = 0
    q = queue.PriorityQueue()
    for n, distance in enumerate(dist):
        q.put((distance, n))
    while not q.empty():
        u = q.get()[1]  # The lowest value entries (by distance) are retrieved first from q.
        if u == t:
            if dist[u] == float('inf'):
                return -1
            return dist[u]
        for i, v in enumerate(adj[u]):
            alt = dist[u] + cost[u][i]
            if alt < dist[v]:
                dist[v] = alt
                q.put((alt, v))
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
