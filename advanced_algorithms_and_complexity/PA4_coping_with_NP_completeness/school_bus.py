# python3

from itertools import permutations
INF = 10 ** 9

from collections import defaultdict


def read_data():
    n, m = 4, 6#map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for x in [[1,2,20], [1,3,42], [1,4,35], [2,3,30], [2,4,34], [3,4,12]]:#range(m):
        u, v, weight = x[0], x[1], x[2]#map(int, input().split())
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
                    continue # skip vertices not in set k

                for j in range(n):
                    if j == i or k & (1 << j) == 0:
                        continue # skip vertices not in set k, also skip i

                    k_without_i = k ^ (1 << i)
                    d_ji = graph[i][j]
                    memo[k][i] = min(memo[k][i], memo[k_without_i][j] + d_ji)

    return min(memo[2 ** n - 1][i] + graph[i][0] for i in range(n))




def optimal_path_slow(graph):
    # This solution tries all the possible sequences of stops.
    n = len(graph)
    best_ans = INF
    best_path = []

    for p in permutations(range(n)):
        cur_sum = 0
        for i in range(1, n):
            if graph[p[i - 1]][p[i]] == INF:
                break
            cur_sum += graph[p[i - 1]][p[i]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum < best_ans:
                best_ans = cur_sum
                best_path = list(p)

    if best_ans == INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])


#if __name__ == '__main__':
#print_answer(*optimal_path(read_data()))

print(optimal_path(read_data()))
