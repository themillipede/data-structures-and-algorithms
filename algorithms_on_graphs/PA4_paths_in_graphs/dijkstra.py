import sys
import queue


def distance(adj, cost, s, t):
    dist = [float('inf') for n in adj]
    dist[s] = 0
    q = queue.PriorityQueue()
    for n, distance in enumerate(dist):
        q.put((distance, n))
    while not q.empty():
        u = q.get()[1]
        if u == t:
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