# python3


def tarjan(graph):

    def strongly_connect(v, index):
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        onstack[v] = True
        for w in graph[v]:
            if indices[w] is None:
                strongly_connect(w, index)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onstack[w]:
                lowlink[v] = min(lowlink[v], lowlink[w])
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

    index = 0
    stack = []
    scc_list = []
    indices = {n: None for n in graph}
    lowlink = {n: None for n in graph}
    onstack = {n: False for n in graph}
    for v in graph:
        if indices[v] is None:
            strongly_connect(v, index)
    return scc_list


def assign_new_colors(n, edges, colours):

    def is_satisfiable():
        graph = {i: [] for i in list(range(-3 * n, 0)) + list(range(1, 3 * n + 1))}
        for i in clauses:
            graph[(-1) * i[0]].append(i[1])
            graph[(-1) * i[1]].append(i[0])
        scc_list = tarjan(graph)
        scc_dict = {v: i for i, sublist in enumerate(scc_list) for v in sublist}
        for x in range(1, 3 * n + 1):
            if scc_dict[x] == scc_dict[(-1) * x]:
                return None
        assignments = {}
        for scc in scc_list:
            for i in scc:
                if i not in assignments:
                    assignments[i] = 1
                    assignments[(-1) * i] = 0
        return assignments

    clauses = []
    colour_to_num = {'R': [1, 2], 'G': [0, 2], 'B': [0, 1]}
    for vertex in range(1, n * 3 + 1, 3):
        cur_colour = colours[int((vertex - 1) / 3)]
        colour_num = colour_to_num[cur_colour]
        clauses.append([vertex + colour_num[0], vertex + colour_num[1]])
        clauses.append([-(vertex + colour_num[0]), -(vertex + colour_num[1])])
    for edge in edges:
        u = (edge[0] - 1) * 3 + 1
        v = (edge[1] - 1) * 3 + 1
        clauses.append([-(u + 0), -(v + 0)])
        clauses.append([-(u + 1), -(v + 1)])
        clauses.append([-(u + 2), -(v + 2)])
    result = is_satisfiable()
    if result:
        num_to_colours = {0: 'R', 1: 'G', 2: 'B'}
        result = [num_to_colours[(i - 1) % 3] for i in range(1, 3 * n + 1) if result[i]]

    return result


def main():
    n, m = map(int, input().split())
    colors = input().split()
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    new_colors = assign_new_colors(n, edges, colors)
    if new_colors is None:
        print("Impossible")
    else:
        print(''.join(new_colors))
