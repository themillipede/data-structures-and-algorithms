# python3

"""
2. Detecting anomalies in currency exchange rates

Introduction: You are given a list of currencies c_1, c_2, ..., c_n together with a list of exchange rates: r_ij
    is the number of units of currency c_j that one gets for one unit of c_i. You would like to check whether it
    is possible to start with one unit of some currency, perform a sequence of exchanges, and get more than one
    unit of the same currency. In other words, you would like to find currencies c_i1, c_i2, ..., c_ik such that
    r_(i1, i2) * r_(i2, i3) * ... * r_(i(k-1), ik) * r_(ik, i1) > 1. For this, you construct the following graph:
    vertices are currencies c_1, c_2, ..., c_n, and the weight of an edge from c_i to c_j is equal to -log(r_ij).
    Then it suffices to check whether there is a negative cycle in the graph. Indeed, if you assume that a cycle
    c_i -> c_j -> c_k -> c_i has a negative weight, then -(log(c_ij) + log(c_jk) + log(c_ki)) < 0 must be true,
    and hence log(c_ij) + log(c_jk) + log(c_ki) > 0. This, in turn, means the following:
    r_ij * r_jk * r_ki = 2^log(c_ij) * 2^log(c_jk) * 2^log(c_ki) = 2^(log(c_ij) + log(c_jk) + log(c_ki)) > 1.

Task: Given a directed graph with edge weights that may be negative, and n vertices and m edges, check whether
    it contains a cycle of negative weight.

Input: A directed graph is given in the standard format.

Constraints: 1 <= n <= 10^3; 0 <= m <= 10^4; edge weights are integers of absolute value at most 10^3.

Output: 1 if the graph contains a cycle of negative weight and 0 otherwise.
"""

import sys


def negative_cycle(adj, cost):
    # add virtual source node
    cost.append([0] * len(adj))
    adj.append(range(len(adj)))

    dist = [float('inf') for _ in adj]
    dist[-1] = 0

    # After a maximum of len(adj) iterations, each vertex will have reached its minimum
    # cost and will not be further reducible, unless the graph contains negative cycles.
    for _ in range(len(adj) - 1):
        for u, vertices in enumerate(adj):
            for i, v in enumerate(vertices):
                alt = dist[u] + cost[u][i]
                if alt < dist[v]:
                    dist[v] = alt

    # If the cost of any vertex can be reduced further, there must be a negative cycle.
    for u, vertices in enumerate(adj):
        for i, v in enumerate(vertices):
            if dist[u] + cost[u][i] < dist[v]:
                return 1
    return 0


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
    print(negative_cycle(adj, cost))
