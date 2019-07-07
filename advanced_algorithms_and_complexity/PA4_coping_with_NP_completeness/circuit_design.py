# python3
import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


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
