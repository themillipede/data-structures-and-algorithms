# python3

"""
1. Assign frequencies to the cells of a GSM network

Introduction: In this problem, you will reduce the real-world problem of assigning frequencies to the transmitting
    towers of the cells in a GSM network to the problem of "proper graph colouring" using 3 colours. Then you will
    design and implement an algorithm to reduce this problem to an instance of SAT.

Task: A GSM network is a type of infrastructure used for communication via mobile phones. It includes transmitting
    towers scattered around the area, which operate at different frequencies. Typically, there is one tower at the
    centre of each tessellating hexagonal region called a cell. A cell phone looks for towers in the neighbourhood
    and decides which one to use based on the strength of the signal as well as some other properties. For a phone
    to distinguish among the few closest towers, the frequencies of the neighbouring towers must be different. You
    are working on a plan for a GSM network, with the restriction that you've only got 3 different frequencies you
    can use in your towers. You know which pairs of towers are neighbours, and for all such pairs both towers must
    use different frequencies. You need to determine whether or not it is possible to assign frequencies to towers
    and satisfy these restrictions.

    This is equivalent to a classical graph colouring problem: in other words, you are given a graph, and you need
    to colour its vertices into 3 different colours, so that any two vertices connected by an edge have different
    colours. Here, colours correspond to frequencies, vertices correspond to cells, and edges connect neighbouring
    cells. Graph colouring is an NP-complete problem, so we do not currently know an efficient solution to it. You
    need to reduce it to an instance of the SAT problem which, though NP-complete, can often be solved efficiently
    in practice using special programs called SAT-solvers.

Input: The first line contains integers n and m -- the number of vertices and edges in the graph. The vertices are
    numbered from 1 through n. Each of the next m lines contains two integers u and v -- the numbers of vertices
    connected by an edge. It is guaranteed that a vertex cannot be connected to itself by an edge.

Constraints: 2 <= n <= 500; 1 <= m <= 1000; 1 <= u, v <= n; u != v.

Output: A boolean formula in the conjunctive normal form (CNF) in a specific format. If it is possible to colour
    the vertices of the input graph in 3 colours such that any two vertices connected by an edge are of different
    colours, the formula must be satisfiable. Otherwise, the formula must be unsatisfiable. The number of variables
    in the formula must be at least 1 and at most 3000. The number of clauses must be at least 1 and at most 5000.

    On the first line, output integers C and V -- the number of clauses in the formula and the number of variables
    respectively. On each of the next C lines, output a description of a single clause. Each clause has the form
    "x_4 OR ~x_1 OR x_8". For a clause with k terms, output first those k terms and then the number 0 at the end
    ("4 -1 8 0" for the example above). Output each term as an integer. Output variables x_1, x_2, ..., x_V as
    numbers 1, 2, ..., V respectively, and negations of variables ~x_1, ~x_2, ..., ~x_V as numbers -1, -2, ..., -V
    respectively. Each number other than the last one in each line must be be a non-zero integer between -V and V,
    where V is the total number of variables specified in the first line of the output. Ensure that 1 <= C <= 5000
    and 1 <= V <= 3000. If there are many different formulas that satisfy the requirements above, you can output
    any one of them.
"""


def get_variable_numbers(vertex_num):
    """
    For a given vertex (identified by integer vertex_num), calculate variable
    numbers for the vertex in each of the three colour variants it could take.
    """
    colour1 = vertex_num * 3
    colour2 = colour1 - 1
    colour3 = colour1 - 2
    return colour1, colour2, colour3


def print_equisatisfiable_sat_formula(num_vertices, num_edges, edges):
    print("%s %s" % (num_edges * 3 + num_vertices, num_vertices * 3))  # Number of clauses and number of variables.
    for vertex in range(1, num_vertices + 1):
        colour1, colour2, colour3 = get_variable_numbers(vertex)
        print("%s %s %s 0" % (colour1, colour2, colour3))  # Each vertex must exist in at least one colour.
    for u, v in edges:
        u_colour1, u_colour2, u_colour3 = get_variable_numbers(u)
        v_colour1, v_colour2, v_colour3 = get_variable_numbers(v)
        print("-%s -%s 0" % (u_colour1, v_colour1))  # u and v cannot both be colour 1.
        print("-%s -%s 0" % (u_colour2, v_colour2))  # u and v cannot both be colour 2.
        print("-%s -%s 0" % (u_colour3, v_colour3))  # u and v cannot both be colour 3.

    # Note that we don't need clauses specifying that each vertex must exist in only one colour, since if it is
    # possible for a vertex to exist in more than one colour, while the edge constraints are satisfied, then it
    # must be the case that the problem is satisfiable also if a vertex is required to exist in one only colour.


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    print_equisatisfiable_sat_formula(n, m, edges)
