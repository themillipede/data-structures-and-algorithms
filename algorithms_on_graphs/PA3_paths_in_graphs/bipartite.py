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
            if adj[n] == adj[node]:
                return 0
            if not adj[n]:
                adj[n] = 2 if adj[node] == 1 else 1
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
