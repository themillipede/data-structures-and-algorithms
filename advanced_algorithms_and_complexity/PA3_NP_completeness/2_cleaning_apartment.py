# python3

"""
2. Cleaning the apartment

Introduction: In this problem, you will determine whether it is possible to clean an apartment after a party
    without leaving any traces of the party. You will reduce it to the classic Hamiltonian Path problem, and
    then you will design and implement an efficient algorithm to reduce it to SAT.

Task: You have just had a huge party in your parents' house, and you need to not only clean the house, but leave
    no trace of the party. To do that, you need to clean all the rooms in some order. After finishing a thorough
    cleaning of some room, you cannot return to it anymore: you are afraid you'll ruin everything accidentally
    and will have to start over. So, you need to move from room to room, visit each room exactly once and clean
    it. You can only move from a room to the neighbouring rooms. You want to determine whether this is possible.

    This can be reduced to a classic Hamiltonian Path problem: given a graph, determine whether there is a route
    visiting each vertex exactly once. Rooms are vertices of the graph, and neighbouring rooms are connected by
    edges. The Hamiltonian Path problem is NP-complete, so we don't know an efficient algorithm to solve it. You
    need to reduce it to SAT, so that it can be solved efficiently by a SAT-solver.

Input: The first line contains two integers n and m -- the number of rooms and the number of corridors connecting
    the rooms, respectively. Each of the next m lines contains two integers u and v describing the corridor going
    from room u to room v. The corridors are two-way, that is, you can go both from u to v and from v to u. No two
    corridors have a common section, that is, each corridor only allows you to go from one room to one other room.
    No corridor connects a room to itself. Note that a corridor from u to v can be listed several times and there
    can be listed both a corridor from u to v and a corridor from v to u.

Constraints: 1 <= n <= 30; 0 <= m <= n(n - 1)/2; 1 <= u, v <= n.

Output: A boolean formula in the CNF form in a specific format. If it is possible to go through all the rooms and
    visit each one exactly once to clean it, the formula must be satisfiable. Otherwise, the formula must be
    unsatisfiable. The sum of the numbers of variables used in each clause of the formula must not exceed 120000.

    On the first line, output integers C and V -- the number of clauses in the formula and the number of variables
    respectively. On each of the next C lines, output a description of a single clause. Each clause has the form
    (x_4 OR ~x_1 OR x_8). For a clause with k terms, output first those k terms and then the number 0 at the end
    ("4 -1 8 0" for the example above). Output each term as an integer. Output variables x_1, x_2, ..., x_V as
    numbers 1, 2, ..., V respectively, and negations of variables ~x_1, ~x_2, ..., ~x_V as numbers -1, -2, ..., -V
    respectively. Each number other than the last one in each line must be be a non-zero integer between -V and V,
    where V is the total number of variables specified in the first line of the output. Ensure that the total
    number of non-zero integers in the C lines describing the clauses is at most 120000. If there are many
    different formulas that satisfy the requirements above, you can output any one of them.
"""

from collections import defaultdict


def print_equisatisfiable_sat_formula():
    result = set()

    for vertex in range(1, n + 1):
        # Each vertex belongs to a path.
        result.add(" ".join([str(i) for i in range(vertex, n * n + 1, n)]) + " 0")
        # Each vertex appears just once in a path.
        for p in range(vertex, n * n, n):
            for q in range(p + n, n * n + 1, n):
                result.add("-%s -%s 0" % (p, q))

    for position in range(1, n * n + 1, n):
        # Each position in a path is occupied by some vertex.
        result.add(" ".join([str(i) for i in range(position, position + n)]) + " 0")
        # No two vertices occupy the same position of a path.
        for p in range(position, position + n - 1):
            for q in range(p + 1, position + n):
                result.add("-%s -%s 0" % (p, q))

    # Two successive vertices on a path must be connected by an edge.
    edge_dict = defaultdict(list)
    for u, v in edges:
        edge_dict[u].append(v)
        edge_dict[v].append(u)
    for vertex in range(1, n + 1):
        for position in range(vertex, n * n + 1 - n, n):
            adj_positions = [adj_node + (position - vertex) + n for adj_node in edge_dict[vertex]]
            result.add("-%s " % (position,) + " ".join([str(i) for i in adj_positions]) + " 0")

    print("%s %s\n" % (len(result), n * n) + "\n".join(result))


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    print_equisatisfiable_sat_formula()
