# python3

n, m = map(int, input().split())
clauses = [list(map(int, input().split())) for i in range(m)]


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


def is_satisfiable():
    graph = {i: [] for i in list(range(-n, 0)) + list(range(1, n + 1))}
    for i in clauses:
        graph[(-1) * i[0]].append(i[1])
        graph[(-1) * i[1]].append(i[0])
    scc_list = tarjan(graph)
    scc_dict = {v: i for i, sublist in enumerate(scc_list) for v in sublist}
    for x in range(1, n + 1):
        if scc_dict[x] == scc_dict[(-1) * x]:
            return None
    assignments = {}
    for scc in scc_list:
        for i in scc:
            if i not in assignments:
                assignments[i] = 1
                assignments[(-1) * i] = 0
    return assignments


result = is_satisfiable()
if result is None:
    print("UNSATISFIABLE")
else:
    print("SATISFIABLE")
    print(" ".join(str(i if result[i] else -i) for i in range(1, n + 1)))
