# python3

"""
1. Integrated circuit design

Introduction: In this problem, you will determine how to connect the modules of an integrated circuit with wires
    so that all the wires can be routed on the same layer of the circuit.

Task: VLSI or Very Large-Scale Integration is a process of creating an integrated circuit by combining thousands
    of transistors on a single chip. You want to design a single layer of an integrated circuit. You know exactly
    what modules will be used, and which of them should be connected by wires. The wires will all be on the same
    layer, but they cannot intersect with each other. Each wire can be bent only once, in one of two directions:
    to the left or to the right. If you connect two modules with a wire, selecting the bending direction uniquely
    defines the position of the wire. Of course, some positions of some pairs of wires lead to intersection, but
    this is forbidden. You need to determine a position for each wire in such a way that no wires intersect.

    This problem can be reduced to the 2-SAT problem, i.e. a special case of the SAT problem in which each clause
    contains exactly 2 variables. For each wire i, denote by x_i a binary variable which takes the value 1 if the
    wire is bent to the right and 0 if the wire is bent to the left. For each i, x_i must be either 0 or 1. Some
    pairs of wires intersect in some positions (e.g. it could be that if wire 1 is bent to the left and wire 2 is
    bent to the right then they intersect). We want a formula that is satisfied only if no wires intersect. There
    will be a clause for each pair of wires in specific positions that would intersect if put in those positions.
    If some pair of wires intersects in any pair of possible positions, we won't be able to design a circuit. You
    need to determine whether it is possible, and if so, determine the direction of bending for each of the wires.

Input: The input represents a 2-CNF formula. The first line contains two integers V and C -- the number of
    variables and the number of clauses, respectively. Each of the next C lines contains two non-zero integers i
    and j, representing a clause in the CNF form. If i > 0, it represents x_i, otherwise if i < 0, it represents
    ~x_i. For example, a line "2 3" represents a clause (x_2 OR x_3), and a line "1 -4" represents (x_1 OR ~x_4).

Constraints: 1 <= V, C <= 1000000; -V <= i, j <= V; i, j != 0.

Output: If the 2-CNF formula in the input is unsatisfiable, output just the word "UNSATISFIABLE". If the formula
    in the input is satisfiable, output the word "SATISFIABLE" on the first line and the corresponding assignment
    of variables on the second line. For each x_i in order from x_1 to x_v, output i if x_i = 1 or -i if x_i = 0.
    For example, if a formula is satisfied by assignment x_1 = 0, x_2 = 1, x_3 = 0, output "-1 2 -3". If there
    are several possible assignments satisfying the input formula, output any one of them.
"""

import sys
import threading

# This code is used to avoid stack overflow issues.
sys.setrecursionlimit(10**6)  # Max depth of recursion.
threading.stack_size(2**26)  # New thread will get stack of such size.


def tarjan(graph):
    """
    Tarjan's algorithm efficiently finds the strongly-connected components (SCCs) of a graph.
    Moreover, the order in which these SCCs are identified constitutes a reverse topological
    sort of the DAG formed by the SCCs.
    """
    index = [0]

    def strongly_connect(v):
        indices[v] = index[0]
        lowlink[v] = index[0]
        index[0] += 1
        stack.append(v)
        onstack[v] = True
        for w in graph[v]:
            if indices[w] is None:
                strongly_connect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onstack[w]:
                lowlink[v] = min(lowlink[v], indices[w])
        if lowlink[v] == indices[v]:
            new_scc = []
            w = stack.pop()
            onstack[w] = False
            new_scc.append(w)
            while w != v:
                w = stack.pop()
                onstack[w] = False
                new_scc.append(w)
            scc_list.append(new_scc)

    stack = []
    scc_list = []
    indices = {n: None for n in graph}
    lowlink = {n: None for n in graph}
    onstack = {n: False for n in graph}
    for v in graph:
        if indices[v] is None:
            strongly_connect(v)
    return scc_list


def is_satisfiable(clauses, num_vars):
    # Construct the implication graph arising from the 2-CNF clauses.
    graph = {i: [] for i in list(range(-num_vars, 0)) + list(range(1, num_vars + 1))}
    for i in clauses:
        if len(i) == 1:
            graph[-i[0]].append(i[0])
        else:
            graph[-i[0]].append(i[1])
            graph[-i[1]].append(i[0])

    # All variables lying in the same SCC of the implication graph should be assigned the same value.
    # This can be understood by considering that if all the edges are satisfied by an assignment and
    # there is a path from x to y (i.e. x implies y) then it cannot be the case that x = 1 and y = 0.
    # So, if a SCC contains a variable together with its negation, then the formula is unsatisfiable.
    scc_list = tarjan(graph)
    scc_dict = {v: i for i, sublist in enumerate(scc_list) for v in sublist}  # Store the SCC of each variable.
    for x in range(1, num_vars + 1):
        if scc_dict[x] == scc_dict[-x]:  # A single SCC contains both x and ~x ==> unsatisfiable!
            return None

    # If no SCC contains a variable together with its negation, then the formula must be satisfiable.
    # A valid assignment of variables can be found by iterating through the SCCs in the order output
    # by Tarjan's algorithm above (i.e. reverse topological order). For each variable that is yet to
    # be assigned in an SCC, set its value to 1, and the value of its negation to 0. The reason we
    # must iterate in REVERSE topological order is that only a proposition which has no implications
    # (or only implications known to be true) can safely be made true without risking contradiction.
    assignments = {}
    for scc in scc_list:
        for i in scc:
            if i not in assignments:
                assignments[i] = 1
                assignments[-i] = 0
    return assignments


def main():
    n, m = map(int, input().split())
    clauses = [list(map(int, input().split())) for i in range(m)]
    result = is_satisfiable(clauses, n)
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join(str(i if result[i] else -i) for i in range(1, n + 1)))


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
