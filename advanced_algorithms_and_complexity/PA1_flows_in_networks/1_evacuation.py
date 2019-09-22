# python3

"""
1. Evacuating people

Introduction: In this problem, you will apply an algorithm for finding maximum flow in a network to determine
    how fast people can be evacuated from a given city.

Task: A tornado is approaching a city, and we need to evacuate the people quickly. There are several roads
    outgoing from the city to the nearest cities, and other roads that go further. The goal is to evacuate
    everybody from the city to the capital, as it is the only other city able to accomodate that many
    newcomers. We need to evacuate everybody as fast as possible, and your task is to find out the maximum
    number of people that can be evacuated each hour given the capacities of all the roads.

Input: The first line of the input contains integers n and m -- the number of cities and the number of roads,
    respectively. Each of the next m lines contains three integers u, v, and c, describing a particular road:
    the start of the road, the end of the road, and the number of people that can be transported through the
    road in one hour. u and v are the 1-based indices of the corresponding cities. The city from which people
    are evacuating is city number 1, and the capital city is city number n.

    Note that all the roads are given as one-directional, that is, you cannot transport people from v to u
    using a road that connects u to v. Note also that there can be multiple roads connecting the same city
    u to the same city v, there can be roads both from u to v and from v to u, there can be roads in only
    one direction, and there can be no roads between a pair of cities. There can also be roads going from
    a city u to itself in the input.

    When evacuating people, they cannot stop in the middle of the road or in any city other than the capital.
    The number of people per hour entering any city other than the evacuating city and the capital city must
    be equal to the number of people per hour exiting from that city. People who have left a city u through
    some road (u, v, c) are assumed to arrive immediately afterwards in the city v. We are interested in the
    maximum possible number of people per hour leaving city 1 under the above restrictions.

Constraints: 1 <= n <= 100; 0 <= m <= 10000; 1 <= u, v <= n; 1 <= c <= 10000. It is guaranteed that
    m * EvacuatePerHour <= 2*10^8, where EvacuatePerHour is the maximum number of people that can be evacuated
    from the city each hour -- the number which you need to output.

Output: A single integer -- the maximum number of people that can be evacuated from city number 1 per hour.
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

    def get_ids(self, start):
        return self.graph[start]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e. id is even), we should get id + 1 due
        # to the described above scheme. On the other hand, when we have to get a "backward" edge for
        # a backward edge (i.e. get a forward edge for backward - id is odd), id - 1 should be taken.
        # It turns out that id ^ 1 works for both cases.
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


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


if __name__ == '__main__':
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    print(max_flow(graph, 0, graph.size() - 1))
