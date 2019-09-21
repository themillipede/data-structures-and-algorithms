# python3

"""
4. Advanced Problem: Reschedule the exams

Introduction: You will design and implement an efficient algorithm to reschedule exams in such a way that every
    student can come to the exam he/she is assigned to, and no two friends will take their exam on the same day.

Task: The new secretary at your Computer Science Department has prepared a schedule of exams for CS-101, and each
    student has been assigned an exam date. However, it is a disaster: not only have some pairs of students known
    to be close friends potentially been assigned the same date, but NONE of the students can actually make it to
    the exam on their assigned day (there was a misunderstanding between the secretary who asked students for the
    dates they were available and the students who understood they needed to select unavailable dates). There are
    three different dates the professors are available for the exams, and these dates cannot be changed. The only
    thing that can be changed is the assignment of students to exam dates. You know that each student cannot come
    on their currently scheduled date, but that each student definitely can come on any of the two other possible
    dates. Also, you must ensure that no two known close friends are assigned to the same exam date. You need to
    determine whether or not this is possible, and if so, suggest a specific assignment of the students to dates.

    This problem can be reduced to a graph problem called 3-recolouring. You are given a graph, and each vertex
    is coloured in one of 3 possible colours. You need to assign a new colour to each vertex in such a way that
    no two vertices connected by an edge are assigned the same colour. The colours correspond to the three exam
    dates, vertices correspond to students, colours of the vertices correspond to the assignment of students to
    the exam dates, and edges correspond to pairs of close friends.

Input: The first line contains two integers n and m -- the number of vertices and the number of edges in the
    graph. The vertices are numbered from 1 to n. The next line contains a string of length n consisting only of
    letters R, G and B, representing the current colour assignments. For each position i (1-based) in the string,
    the letter in that position corresponds to the current colour of vertex i. Each of the current colour
    assignments must be changed. Each of the next m lines contains two integers u and v -- vertices u and v are
    connected by an edge (it is possible that u = v).

Constraints: 1 <= n <= 1000; 0 <= m <= 20000; 1 <= u, v <= n.

Output: If it is impossible to reassign the students to the dates of exams in such a way that no two friends are
    going to take the exam the same day, and each student's assigned date has changed, output just "Impossible".
    Otherwise, output one string consisting of n characters R, G and B representing the new colouring of the
    vertices. Note that the colour of each vertex must be different from the initial colour of that vertex. The
    vertices connected by an edge must have different colours.
"""


##################################################
# SAT solver code created in "1_circuit_design.py"
##################################################


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
    # be assigned in an SCC, set its value to 1, and the value of its negation to 0.
    assignments = {}
    for scc in scc_list:
        for i in scc:
            if i not in assignments:
                assignments[i] = 1
                assignments[-i] = 0
    return assignments


##################################################
# Solution for this problem using SAT solver above
##################################################


def assign_new_colours(n, edges, colours):
    clauses = []
    for vertex in range(1, n + 1):
        colour_num = 'BGR'.index(colours[vertex - 1])
        alt_colour1 = vertex * 3 - (colour_num + 1) % 3
        alt_colour2 = vertex * 3 - (colour_num + 2) % 3
        clauses.append([-(vertex * 3 - colour_num)])
        clauses.append([alt_colour1, alt_colour2])
        clauses.append([-alt_colour1, -alt_colour2])
    for u, v in edges:
        clauses.append([-(u * 3 - 2), -(v * 3 - 2)])  # u and v cannot both be 'R'.
        clauses.append([-(u * 3 - 1), -(v * 3 - 1)])  # u and v cannot both be 'G'.
        clauses.append([-(u * 3 - 0), -(v * 3 - 0)])  # u and v cannot both be 'B'.
    result = is_satisfiable(clauses, n * 3)
    if result:
        # 'R' = 1, 4, 7, etc. 'G' = 2, 5, 8, etc. 'B' = 3, 6, 9, etc.
        result = ['RGB'[i % 3] for i in range(n * 3) if result[i + 1]]
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    colours = input()
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    new_colours = assign_new_colours(n, edges, colours)
    if new_colours is None:
        print("Impossible")
    else:
        print(''.join(new_colours))
