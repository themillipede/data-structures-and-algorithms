# python3

"""
3. School bus

Introduction: In this problem, you will determine the fastest route for a school bus to start from the depot,
    visit all the children's homes, get them to school, and return back to the depot.

Task: A school bus needs to start from the depot early in the morning, pick up all the children from their homes
    in some order, get them all to school, and return to the depot. You know the time it takes to get from depot
    to each home, from each home to each other home, from each home to the school, and from the school to the
    depot. You want to define the order in which to visit children's homes so as to minimize the total time spent
    on the route.

    This is an instance of a classical NP-complete problem called the Traveling Salesman Problem. Given a graph
    with weighted edges, you need to find the shortest cycle visiting each vertex exactly once. In this problem,
    vertices correspond to homes, the school and the depot. Edge weights correspond to the time to get from one
    vertex to another. Some vertices may not be connected by an edge in the general case.

Input: The first line contains two integers n and m -- the numbers of vertices and edges in the graph. The
    vertices are numbered from 1 to n. Each of the next m lines contains three integers u, v and t, representing
    an edge of the graph. This edge connects vertices u and v, and it takes time t to get from u to v. The edges
    are bidirectional: you can go both from u to v and from v to u in time t using the edge in question. No edge
    connects a vertex to itself. No two vertices are connected by more than one edge.

Constraints: 2 <= n <= 17; 1 <= m <= n(n - 1)/2; 1 <= u, v <= n; u!= v; 1 <= t <= 1000000.

Output: If it is possible to start at some vertex, visit each other vertex exactly once in some order via edges
    of the graph, and return to the starting vertex, output two lines. On the first line, output the minimum
    possible time to go through this circular route visiting all vertices exactly once (apart from the first
    vertex which is visited twice -- at the beginning and at the end). On the second line, output the order in
    which you should visit the vertices to get the minimum possible time on the route. That is, output numbers
    1 to n in the order that those vertices will be visited. Don't output the starting vertex the second time.
    However, account for the time to get from the last vertex back to the starting vertex. If there are several
    solutions, output any one of them. If there is no such circular route, output just -1 on a single line. Note
    that for n = 2 it is considered a correct circular route to go from one vertex to the other and back again
    via the same edge.
"""

from collections import defaultdict

INF = 10 ** 9


def optimal_path(graph):
    n = len(graph)

    # For every possible subset of vertices (excluding those that don't contain the starting vertex 0) taken
    # from the full set of n vertices, keep track, for each vertex in a subset, of the minimum time to reach
    # that vertex via a route that starts at vertex 0 and visits all other vertices in the subset once.
    memo = [[float('inf') for _ in range(n)] for _ in range(2 ** n)]

    # The minimum time to get from vertex 0 to vertex 0 in the subset containing only vertex 0 is 0. Note that
    # we don't start with memo[0][0], as memo[0] corresponds to the empty set, which doesn't contain vertex 0.
    memo[1][0] = 0

    # All subsets must include vertex 0, so we only need to keep track of the other vertices, hence we only go
    # through subsets from 0 to 2 ** (n - 1). Since we are using binary representations of the subset numbers,
    # in practice this means that we can number each subset as it would be with vertex 0 included, but shifted
    # one bit to the right, so that the rightmost bit now corresponds to vertex 1. To obtain the number of the
    # full subset (including vertex 0), we just need to shift the binary representation of the reduced subset
    # (excluding vertex 0) one place to the left, and add 1. For example, the subset containing vertices 0, 1,
    # and 3 is represented in binary as 1011, which corresponds to a subset number of 11. Since we do not need
    # to consider vertex 0, we can move this one place to the right, giving a reduced subset number of 5.

    # For each possible subset size (i.e. for each integer between 0 and n - 1), record which integers between 0
    # and 2 ** (n - 1) have a binary representation in which the number of set bits is equal to that subset size.
    sets_by_size = defaultdict(list)
    for i in range(2 ** (n - 1)):

        # Find the number of vertices (excluding vertex 0) in the i-th subset, which
        # is equivalent to the number of set bits in the binary representation of i.
        num_vertices = sum((i & (1 << num)) >> num for num in range(n - 1))

        # Add i to the list of subsets that contain num_vertices vertices in total
        # (i.e. those whose binary representations contain num_vertices set bits).
        sets_by_size[num_vertices].append(i)

    # Iterate through subsets of vertices in order of increasing subset size. We iterate according to subset
    # size rather than subset number because the number of set bits in the binary representation of a subset
    # number (which corresponds to the subset size) does not necessarily increase with subset number.
    for subset_size in range(2, n + 1):

        # Iterate through each subset that has (subset_size - 1) vertices not including vertex 0
        # (i.e. whose subset number has (subset_size - 1) set bits in its binary representation).
        for k_without_zero in sets_by_size[subset_size - 1]:

            # Get the subset number for subset k_without_zero once vertex 0 is included.
            k = (k_without_zero << 1) + 1

            # Iterate through all vertices in subset k except vertex 0.
            for i in range(1, n):
                if k & (1 << i) == 0:
                    continue  # Skip vertices not in set k.

                # Iterate through vertices in subset k, except vertex i (but including vertex 0).
                for j in range(n):
                    if j == i or k & (1 << j) == 0:
                        continue  # Skip vertices not in set k, also skip vertex i.

                    # Create new subset that does not include i, and update
                    # the minimum distance for subset k starting at vertex 0 and
                    # ending at vertex i, with j as the penultimate vertex.
                    k_without_i = k ^ (1 << i)
                    d_ji = graph[i][j]
                    memo[k][i] = min(memo[k][i], memo[k_without_i][j] + d_ji)

    distance = min(memo[2 ** n - 1][i] + graph[i][0] for i in range(n))

    if distance >= INF:
        return -1, []

    # Backtracking to find the shortest path.
    path = []
    remaining_node_set = 2 ** n - 1  # Start with the set of all nodes.

    while remaining_node_set > 0:
        current_node = path[0] if len(path) > 0 else 0
        remaining_nodes = [i for i in range(n) if (remaining_node_set & (1 << i)) > 0]
        prev_node = min(remaining_nodes, key=lambda k: memo[remaining_node_set][k] + graph[k][current_node])
        path = [prev_node] + path
        # Remove the selected previous node from the remaining node set.
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
