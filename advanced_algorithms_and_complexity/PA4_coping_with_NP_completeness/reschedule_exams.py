# python3

# 4. Advanced Problem: Reschedule the exams
# Task: The new secretary at your Computer Science Department has prepared a schedule of exams for CS-101: each
#     student was assigned to his own exam date. However, it's a disaster: not only some pairs of students known to
#     be close friends may have been assigned the same date, but also NONE of the students can actually come to the
#     exam at the day they were assigned (there was a misunderstanding between the secretary who asked to specify
#     available dates and the students who understood they needed to select unavailable dates). There are three
#     different dates the professors are available for these exams, and these dates cannot be changed. The only
#     thing that can be changed is the assignment of students to the dates of exams. You know for sure that each
#     student can't come at the currently scheduled date, but also each student definitely can come at any of the
#     two other possible dates. Also, you must make sure that no two known close friends are assigned to the same
#     exam date. You need to determine whether it is possible or not, and if yes, suggest a specific assignment of
#     the students to the dates. This problem can be reduced to a graph problem called 3-recolouring. You are given
#     a graph, and each vertex is coloured in one of the 3 possible colours. You need to assign another colour to
#     each vertex in such a way that no two vertices connected by and edge are assigned the same colour. Possible
#     colours correspond to the possible exam dates, vertices correspond to students, colours of the vertices
#     correspond to the assignment of students to the exam dates, and edges correspond to pairs of close friends.
# Input: The first line contains two integers n and m -- the number of vertices and the number of edges in the
#     graph. The vertices are numbered from 1 through n. The next line contains a string of length n consisting
#     only of letters R, G and B, representing the current colour assignments. For each position i (1-based) in the
#     string, the letter in that position corresponds to the current colour of vertex i. Each of the current colour
#     assignments must be changed. Each of the next m lines contains two integers u and v -- vertices u and v are
#     connected by an edge (it is possible that u = v).
# Constraints: 1 <= n <= 1000; 0 <= m <= 20000; 1 <= u, v <= n.
# Output: If it is impossible to reassign the students to the dates of exams in such a way that no two friends are
#     going to take the exam the same day, and each student's assigned date has changed, output just "Impossible".
#     Otherwise, output one string consisting of n characters R, G and B representing the new colouring of the
#     vertices. Note that the colour of each vertex must be different from the initial colour of that vertex. The
#     vertices connected by an edge must have different colours.


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


def assign_new_colors(n, edges, colours):
    clauses = []
    colour_to_other_num = {'R': [1, 2], 'G': [0, 2], 'B': [0, 1]}
    colour_to_num = {'R': 0, 'G': 1, 'B': 2}
    for vertex in range(1, n * 3 + 1, 3):
        cur_colour = colours[(vertex - 1) // 3]
        clauses.append([-(vertex + colour_to_num[cur_colour])])
        colour_num = colour_to_other_num[cur_colour]
        clauses.append([vertex + colour_num[0], vertex + colour_num[1]])
        clauses.append([-(vertex + colour_num[0]), -(vertex + colour_num[1])])
    for edge in edges:
        u = (edge[0] - 1) * 3 + 1
        v = (edge[1] - 1) * 3 + 1
        clauses.append([-(u + 0), -(v + 0)])
        clauses.append([-(u + 1), -(v + 1)])
        clauses.append([-(u + 2), -(v + 2)])
    result = is_satisfiable(clauses, n * 3)
    if result:
        result = ['RGB'[i % 3] for i in range(n * 3) if result[i + 1]]
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    colours = input()
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    new_colours = assign_new_colors(n, edges, colours)
    if new_colours is None:
        print("Impossible")
    else:
        print(''.join(new_colours))
