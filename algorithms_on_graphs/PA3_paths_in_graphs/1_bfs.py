# python3
import sys
import queue


def distance(adj, s, t):
    visited = [0] * len(adj)
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        n = q.get()
        num_edges = visited[n] + 1
        for node in adj[n]:
            if node == t:
                return num_edges
            if not visited[node]:
                visited[node] = num_edges
                q.put(node)
    return -1


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
