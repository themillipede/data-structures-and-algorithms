# python3

"""
2. Assigning airline crews to flights

Introduction: In this problem, you will apply an algorithm for finding maximum matching in a bipartite graph
    to assign airline crews to flights in the most efficient way.

Task: The airline offers a bunch of flights and has a set of crews that can work on those flights. However,
    the flights are starting in different cities and at different times, so only some of the crews are able
    to work on a particular flight. You are given the pairs of flights and associated crews that can work on
    those flights. You need to assign crews to as many flights as possible and output all the assignments.

Input: The first line contains integers n and m -- the number of flights and the number of crews, respectively.
    Each of the next n lines contains m binary integers (0 or 1). If the j-th integer in the i-th line is 1,
    then crew number j can work on the flight number i, and if it is 0, then it cannot.

Constraints: 1 <= n, m <= 100.

Output: Output n integers -- for each flight, output the 1-based index of the crew assigned to that flight. If
    no crew is assigned to a flight, output -1 as the index of the crew assigned to it. All the positive
    indices in the output must be between 1 and m, and they must be pairwise different, but you can output any
    number of -1's. If there are several assignments with the maximum possible number of flights having a crew
    assigned, output any of them.
"""

import queue


class Edge:
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


class FlowGraph:
    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n)]

    def add_edge(self, start, end, capacity):
        forward_edge = Edge(start, end, capacity)
        backward_edge = Edge(end, start, 0)
        self.graph[start].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[end].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, start):
        return self.graph[start]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def transform_data(g):
    vertex_count, edge_count = len(g), sum(len(i) for i in g)
    graph = FlowGraph(vertex_count)
    for n, vertex in enumerate(g):
        for i in vertex:
            u, v, capacity = n, i, 1
            graph.add_edge(u, v, capacity)
    return graph


def max_flow(graph, source, sink):
    flow = 0
    while True:
        q = queue.Queue()
        q.put(source)
        pred = [None for _ in graph.graph]
        while not q.empty() and not pred[sink]:
            nodenum = q.get()
            edges = graph.get_ids(nodenum)
            for id in edges:
                edge = graph.get_edge(id)
                if pred[edge.v] is None and edge.v != source and edge.capacity > edge.flow:
                    pred[edge.v] = id
                    q.put(edge.v)
        if pred[sink] is not None:
            node = sink
            path = []
            while node > 0:
                id = pred[node]
                path.append(id)
                node = graph.get_edge(id).u
            path.reverse()
            minflow = float('inf')
            for id in path:
                edge = graph.get_edge(id)
                if edge.capacity - edge.flow < minflow:
                    minflow = edge.capacity - edge.flow
            for edge in path:
                graph.add_flow(edge, minflow)
            flow += minflow
        else:
            break
    return flow


def find_matching(adj_matrix):
    n = len(adj_matrix)
    m = len(adj_matrix[0])
    graph = [[] for _ in range(n + m + 2)]
    graph[0] += range(1, n + 1)
    for i in range(n):
        for j in range(m):
            if adj_matrix[i][j]:
                graph[i + 1].append(j + 1 + n)
    for j in range(m):
        graph[n + 1 + j].append(len(graph) - 1)
    flowgraph = transform_data(graph)
    max_flow(flowgraph, 0, n + m + 1)
    matching = [-1 for _ in range(n)]
    for i, edge in enumerate(flowgraph.edges):
        if edge.flow == 1 and edge.u in range(1, 1 + n):
            matching[edge.u - 1] = edge.v - (1 + n)
    return matching


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_matrix = [list(map(int, input().split())) for i in range(n)]
    matching = find_matching(adj_matrix)
    line = [str(-1 if x == -1 else x + 1) for x in matching]
    print(' '.join(line))