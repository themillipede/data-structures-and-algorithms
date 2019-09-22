# python3

"""
3. Clustering

Introduction: Clustering is a fundamental problem in data mining. The goal is to partition a given set of objects
    into subsets (or clusters) in such a way that any two objects from the same subset are close (or similar) to
    each other, while any two objects from different subsets are far apart.

Task: Given n points on a plane and an integer k, compute the largest possible value of d such that the given
    points can be partitioned into k non-empty subsets in such a way that the distance between any two points
    from different subsets is at least d.

Input: The first line contains the number of points n. Each of the following n lines defines a point (x_i, y_i).
    The last line contains the number of clusters k.

Constraints: 2 <= k <= n <= 200; -10^3 <= x_i, y_i <= 10^3 are integers. All points are pairwise different.

Output: The largest value of d. The absolute value of the difference between the answer of your program and the
    optimal value should be at most 10^-6.
"""

import sys
import math


def get_squared_distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(i, j, parent, rank):
    i_parent = find(i, parent)
    j_parent = find(j, parent)
    if i_parent == j_parent:
        return
    if rank[i_parent] > rank[j_parent]:
        parent[j_parent] = i_parent
    else:
        parent[i_parent] = j_parent
        if rank[i_parent] == rank[j_parent]:
            rank[j_parent] += 1


def clustering(x, y, k):
    n = len(x)
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            squared_dist = get_squared_distance(x[i], y[i], x[j], y[j])
            edges.append([squared_dist, i, j])
    edges.sort()
    idx = 0
    # While the number of clusters (which starts as the number of points, n) is larger than
    # the required number of clusters k, assign the two nearest points to the same cluster.
    while n > k:
        if find(edges[idx][1], parent) != find(edges[idx][2], parent):
            union(edges[idx][1], edges[idx][2], parent, rank)
            n -= 1
        idx += 1
    # Find the pair of points, not in the same cluster, separated by the smallest distance.
    while find(edges[idx][1], parent) == find(edges[idx][2], parent):
        idx += 1
    return math.sqrt(edges[idx][0])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
