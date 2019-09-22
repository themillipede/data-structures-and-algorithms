# python3

"""
1. Building roads to connect cities

Introduction: The goal in this problem is to build roads between some pairs of the given cities such that there
    is a path between any two cities and the total length of the roads is minimized.

Task: Given n points on a plane, connect them with segments of minimum total length such that there is a path
    between any two points.

Input: The first line contains the number of points n. Each of the following n lines defines a point (x_i, y_i).

Constraints: 1 <= n <= 200; -10^3 <= x_i, y_i <= 10^3 are integers; all points are pairwise different; no three
    points lie on the same line.

Output: The minimum total length of segments. The absolute value of the difference between the answer of your
    program and the optimal value should be at most 10^-6.
"""

import sys
import math


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


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


def minimum_distance(x, y):
    result = 0
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            dist = get_distance(x[i], y[i], x[j], y[j])
            edges.append([dist, i, j])
    edges.sort()
    for edge in edges:
        if find(edge[1], parent) != find(edge[2], parent):
            result += edge[0]
            union(edge[1], edge[2], parent, rank)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
