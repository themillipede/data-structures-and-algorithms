# python3

from collections import defaultdict

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]


def print_equisatisfiable_sat_formula():

    result = []

    for vertex in range(1, n + 1):
        # Each vertex belongs to a path
        result.append(" ".join([str(i) for i in range(vertex, n * n + 1, n)]) + " 0")
        # Each vertex appears just once in a path
        for p in range(vertex, n * n, n):
            for q in range(p + 5, n * n + 1, n):
                result.append("-%s -%s 0" % (p, q))

    for position in range(1, n * n + 1, n):
        # Each position in a path is occupied by some vertex
        result.append(" ".join([str(i) for i in range(position, position + n)]) + " 0")
        # No two vertices occupy the same position of a path
        for p in range(position, position + n - 1):
            for q in range(p + 1, position + n):
                result.append("-%s -%s 0" % (p, q))

    # Two successive vertices on a path must be connected by an edge
    edge_dict = defaultdict(list)
    for edge in edges:
        u = edge[0]
        v = edge[1]
        edge_dict[u].append(v)
        edge_dict[v].append(u)
    for vertex in range(1, n + 1):
        for position in range(vertex, n * n + 1 - n, n):
            adj_positions = [adj_node + (position - vertex) + n for adj_node in edge_dict[vertex]]
            result.append("-%s " % (position,) + " ".join([str(i) for i in adj_positions]) + " 0")

    print("%s %s\n" % (len(result), n * n) + "\n".join(result))


print_equisatisfiable_sat_formula()
