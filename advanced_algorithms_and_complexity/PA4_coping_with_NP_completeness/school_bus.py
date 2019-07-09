# python3
from collections import defaultdict

INF = 10 ** 9

# 3. School bus
# Task: A school bus needs to start from the depot early in the morning, pick up all the children from their homes
#     in some order, get them all to school, and return to the depot. You know the time it takes to get from depot
#     to each home, from each home to each other home, from each home to the school, and from the school to the
#     depot. You want to define the order in which to visit children's homes so as to minimize the total time spent
#     on the route. This is an instance of a classical NP-complete problem called Traveling Salesman Problem. Given
#     a graph with weighted edges, you need to find the shortest cycle visiting each vertex exactly once. Vertices
#     correspond to homes, the school, and the depot. Edge weights correspond to the time to get from one vertex to
#     another. Some vertices may not be connected by an edge in the general case.
# Input: The first line contains two integers n and m -- the numbers of vertices and edges in the graph. The
#     vertices are numbered from 1 to n. Each of the next m lines contains three integers u, v and t, representing
#     an edge of the graph. This edge connects vertices u and v, and it takes time t to get from u to v. The edges
#     are bidirectional: you can go both from u to v and from v to u in time t using the edge in question. No edge
#     connects a vertext to itself. No two vertices are connected by more than one edge.
# Constraints: 2 <= n <= 17; 1 <= m <= n(n - 1)/2; 1 <= u, v <= n; u!= v; 1 <= t <= 1000000.
# Output: If it is possible to start at some vertex, visit each other vertex exactly once in some order via edges
#     of the graph, and return to the starting vertex, output two lines. On the first line, output the minimum
#     possible time to go through such circular route visiting all vertices exactly once (apart from the first
#     vertex which is visited twice -- at the beginning and at the end). On the second line, output the order in
#     which you should visit the vertices to get the minimum possible time on the route. That is, output numbers
#     1 t n in the order corresponding to visiting the vertices. Don't output the starting vertex the second time.
#     However, account for the time to get from the last vertex back to the starting vertex. If there are several
#     solutions, output any one of them. If there is no such circular route, output just -1 on a single line. Note
#     that for n = 2 it is considered a correct circular route to go from one vertex to the other and back again
#     via the same edge.


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
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    path_weight, path = optimal_path(graph)
    if path_weight != -1:
        print(' '.join(map(str, path)))
