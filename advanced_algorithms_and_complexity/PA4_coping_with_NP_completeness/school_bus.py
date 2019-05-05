# python3
from collections import defaultdict

INF = 10 ** 9


def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for x in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph


def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))


def optimal_path(graph):
    n = len(graph)
    memo = [[float('inf') for _ in range(n)] for _ in range(2 ** n)]
    memo[1][0] = 0

    # all sets should include 0, so we only account for the other elements,
    # hence we only go through the sets up to 2 ** (n - 1).
    sets_by_size = defaultdict(list)
    for i in range(2 ** (n - 1)):
        size = sum((i & (1 << num)) >> num for num in range(n - 1))
        sets_by_size[size].append(i)

    for subset_size in range(2, n + 1):
        for k_without_zero in sets_by_size[subset_size - 1]:
            k = (k_without_zero << 1) + 1

            for i in range(1, n):
                if k & (1 << i) == 0:
                    continue  # skip vertices not in set k

                for j in range(n):
                    if j == i or k & (1 << j) == 0:
                        continue  # skip vertices not in set k, also skip i

                    k_without_i = k ^ (1 << i)
                    d_ji = graph[i][j]
                    memo[k][i] = min(memo[k][i], memo[k_without_i][j] + d_ji)

    distance = min(memo[2 ** n - 1][i] + graph[i][0] for i in range(n))

    if distance >= INF:
        return -1, []

    # backtracking to find the shortest path
    path = []
    remaining_node_set = 2 ** n - 1  # start with the set of all nodes

    while remaining_node_set > 0:
        current_node = path[0] if len(path) > 0 else 0
        remaining_nodes = [i for i in range(n) if (remaining_node_set & (1 << i)) > 0]
        prev_node = min(remaining_nodes, key=lambda k: memo[remaining_node_set][k] + graph[k][current_node])
        path = [prev_node] + path
        # remove the selected previous node from the remaining node set
        remaining_node_set = remaining_node_set ^ (1 << prev_node)

    return distance, [p + 1 for p in path]


if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
