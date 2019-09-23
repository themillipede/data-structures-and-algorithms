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


if __name__ == '__main__':
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    print(max_flow(graph, 0, graph.size() - 1))
