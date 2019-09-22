# python3

"""
3. Advanced Problem: Exchanging money optimally

Introduction: Now, you would like to compute an optimal way of exchanging the given currency c_i into all other
    currencies. For this, you find shortest paths from the vertex c_i to all the other vertices.

Task: Given a directed graph with edge weights that may be negative, and n vertices and m edges as well as the
    vertex s, compute the lengths of the shortest paths from s to all other vertices of the graph.

Input: A directed graph is given in the standard format.

Constraints: 1 <= n <= 10^3; 0 <= m <= 10^4; 1 <= s <= n; edge weights are integers of absolute value at most 10^9.

Output: For all vertices i from 1 to n, output the following on a separate line:
    - "*" if there is no path from s to u;
    - "-" if there is a path from s to u, but there is no shortest path from s to u (i.e. distance(s->u) = -inf);
    - The length of the shortest path otherwise.
"""

import sys
import queue


def shortest_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    reachable[s] = 1
    for _ in range(len(adj) - 1):
        for u, vertices in enumerate(adj):
            for i, v in enumerate(vertices):
                alt_distance = distance[u] + cost[u][i]
                if alt_distance < distance[v]:
                    distance[v] = alt_distance
                    reachable[v] = 1
    relaxed_vertices = set()
    for u, vertices in enumerate(adj):
        for i, v in enumerate(vertices):
            alt_distance = distance[u] + cost[u][i]
            if alt_distance < distance[v]:
                relaxed_vertices.add(v)
    q = queue.Queue()
    for node in relaxed_vertices:
        q.put(node)
    reached = set()
    while not q.empty():
        n = q.get()
        reached.add(n)
        shortest[n] = 0
        for node in adj[n]:
            if node not in reached:
                q.put(node)


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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
