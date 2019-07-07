# python3


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
