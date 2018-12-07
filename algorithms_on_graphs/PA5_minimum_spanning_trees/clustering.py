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
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            squared_dist = get_squared_distance(x[i], y[i], x[j], y[j])
            edges.append([squared_dist, i, j])
    edges.sort()
    idx = 0
    while len(set(parent)) > k:
        if find(edges[idx][1], parent) != find(edges[idx][2], parent):
            union(edges[idx][1], edges[idx][2], parent, rank)
        idx += 1
    while find(edges[idx][1], parent) == find(edges[idx][2], parent):
        idx += 1
    shortest_distance = math.sqrt(edges[idx][0])
    return shortest_distance


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
