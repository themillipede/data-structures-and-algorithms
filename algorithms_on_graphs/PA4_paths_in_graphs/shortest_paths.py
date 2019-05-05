# python3
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
