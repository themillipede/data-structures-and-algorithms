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
