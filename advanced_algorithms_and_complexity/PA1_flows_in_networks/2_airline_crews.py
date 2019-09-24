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


# This class has an unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:
    def __init__(self, n):
        self.edges = []  # List of all (forward and backward) edges.
        self.graph = [[] for _ in range(n)]  # This adjacency list stores only indices of edges in the edges list.

    def add_edge(self, start, end, capacity):
        # Note that we first append a forward edge and then a backward edge, so all forward edges are
        # stored at even indices (starting from 0), whereas backward edges are stored at odd indices.
        forward_edge = Edge(start, end, capacity)
        backward_edge = Edge(end, start, 0)
        self.graph[start].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[end].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_edge_ids(self, start):
        return self.graph[start]

    def get_edge(self, edge_id):
        return self.edges[edge_id]

    def add_flow(self, edge_id, flow):
        # To get a backward edge for a true forward edge (i.e. edge_id is even), we use edge_id + 1.
        # But to get a "backward" edge for a backward edge (i.e. edge_id is odd), we use edge_id - 1.
        # Conveniently, edge_id ^ 1 gives the correct edge from which to subtract flow in both cases.
        self.edges[edge_id].flow += flow
        self.edges[edge_id ^ 1].flow -= flow


############################################
# Max flow code created in "1_evacuation.py"
############################################

def max_flow(graph, source, sink):
    flow = 0
    while True:

        # Use BFS to find the shortest augmenting
        # path (by number of edges) if one exists.
        q = queue.Queue()
        q.put(source)
        incoming_edge = [None for _ in graph.graph]  # To store the edge taken to get to each vertex.
        while not q.empty() and not incoming_edge[sink]:
            nodenum = q.get()
            edges = graph.get_edge_ids(nodenum)
            for edge_id in edges:
                edge = graph.get_edge(edge_id)
                remaining_capacity = edge.capacity - edge.flow
                if incoming_edge[edge.v] is None and edge.v != source and remaining_capacity > 0:
                    incoming_edge[edge.v] = edge_id
                    q.put(edge.v)

        if incoming_edge[sink] is not None:  # Check there is actually an augmenting path.
            node = sink
            path = []

            # Backtrack from sink to source to recover
            # the edge path taken from source to sink.
            while node > 0:
                edge_id = incoming_edge[node]
                path.append(edge_id)
                node = graph.get_edge(edge_id).u
            path.reverse()

            # Find the maximum possible flow in the augmenting path (which is equal to the remaining
            # capacity of the edge with the minimum remaining capacity among the edges in the path).
            minflow = float('inf')
            for edge_id in path:
                edge = graph.get_edge(edge_id)
                remaining_capacity = edge.capacity - edge.flow
                if remaining_capacity < minflow:
                    minflow = remaining_capacity

            # Add the flow calculated for the augmenting path
            # to the flow of each edge in the augmenting path.
            for edge_id in path:
                graph.add_flow(edge_id, minflow)

            # Increase the maximum flow of the network by the
            # value of the flow found in the augmenting path.
            flow += minflow

        # The flow through a graph is optimal
        # iff it contains no augmenting path.
        else:
            break
    return flow


############################################
# Solution for this problem using "max_flow"
############################################

def transform_data(g):
    vertex_count, edge_count = len(g), sum(len(i) for i in g)
    graph = FlowGraph(vertex_count)
    for n, vertex in enumerate(g):
        for i in vertex:
            u, v, capacity = n, i, 1
            graph.add_edge(u, v, capacity)
    return graph


def find_matching(adj_matrix):
    n = len(adj_matrix)  # Number of flights.
    m = len(adj_matrix[0])  # Number of crews.
    graph = [[] for _ in range(n + m + 2)]  # Two extra nodes for dummy source and dummy sink.
    graph[0] += range(1, n + 1)  # Connect dummy source to every flight.
    for i in range(n):
        for j in range(m):
            if adj_matrix[i][j]:
                graph[1 + i].append(1 + n + j)  # Make the "flow" direction one-way (from flights to crews).
    for j in range(m):
        graph[1 + n + j].append(len(graph) - 1)  # Connect every crew to dummy sink.
    flowgraph = transform_data(graph)
    max_flow(flowgraph, 0, n + m + 1)  # Graph, source, sink.
    matching = [-1 for _ in range(n)]
    for i, edge in enumerate(flowgraph.edges):
        if edge.flow == 1 and edge.u in range(1, 1 + n):  # Edge starts at a flight and has flow (to a crew).
            matching[edge.u - 1] = edge.v - (1 + n)  # Recover crew and flight numbers from node numbers.
    return matching


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_matrix = [list(map(int, input().split())) for i in range(n)]
    matching = find_matching(adj_matrix)
    line = [str(-1 if x == -1 else x + 1) for x in matching]
    print(' '.join(line))
