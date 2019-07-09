# python3
import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

# 1. Integrated circuit design
# Task: VLSI or Very Large-Scale Integration is a process of creating an integrated circuit by combining thousands
#     of transistors on a single chip. we want to design a single layer of an integrated circuit. We know exactly
#     what modules will be used, and which of them should be connected by wires. The wires will all be on the same
#     layer, but they cannot intersect with each other. Each wire can be bent once, in one of two directions -- to
#     the left or to the right. If we connect two modules with a wire, selecting the direction of bending uniquely
#     defines the position of the wire. Some wire positions lead to intersection of two wires, which is forbidden.
#     The task is to determine a position for each wire in such a way that no wires intersect. This problem can be
#     reduced to the 2-SAT problem. For each wire i, we denote by x_i a binary variable which takes value 1 if the
#     wire is bent to the right and 0 if the wire is bent to the left. For each i, x_i must be either 0 or 1. Some
#     pairs of wires intersect in some positions. We want a formula that is satisfied only if no wires intersect.
#     There will be a clause for each wire/position pair that could potentially intersect (e.g. wire 1 is directly
#     to the right of wire 2, and wire 1 is bent to the the left and wire 2 is bent to the right). If some pair of
#     wires intersects in any pair of possible positions, we won't be able to design a circuit. The task is to
#     determine whether it is possible, and if yes, determine the direction of bending for each of the wires.
# Input: This represents a 2-CNF formula. The first line contains two integers V and C -- the number of variables
#     and the number of clauses respectively. Each of the next C lines contains two non-zero integers i and j
#     representing a clause in the CNF form. If i > 0, it represents x_i, otherwise if i <0, it represents ~x_i.
#     For example, a line "2 3" represents a clause (x_2 OR x_3), and line "1 -3" represents (x_1 OR ~x_4).
# Constraints: 1 <= V, C <= 1000000; -V <= i, j <= V; i, j != 0.
# Output: If the 2-CNF formula in the input is unsatisfiable, output just the word "UNSATISFIABLE". If the formula
#     in the input is satisfiable, output the word "SATISFIABLE" on the first line and the corresponding assignment
#     of variables on the second line. For each x_i in order from x_1 to x_v, output i if x_i = 1 or -i if x_i = 0.
#     For example, if a formula is satisfied by assignment x_1 = 0, x_2 = 1, x_3 = 0, output "-1 2 -3". If there
#     are several possible assignments satisfying the input formula, output any one of them.


def tarjan(graph):
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
    graph = {i: [] for i in list(range(-num_vars, 0)) + list(range(1, num_vars + 1))}
    for i in clauses:
        if len(i) == 1:
            graph[-i[0]].append(i[0])
        else:
            graph[-i[0]].append(i[1])
            graph[-i[1]].append(i[0])
    scc_list = tarjan(graph)
    scc_dict = {v: i for i, sublist in enumerate(scc_list) for v in sublist}
    for x in range(1, num_vars + 1):
        if scc_dict[x] == scc_dict[-x]:
            return None
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
