# python3

"""
3. Advanced Problem: Stock charts

Introduction: In this problem you will find the most compact way of visualizing stock price data using charts.

Task: You are in the middle of writing your newspaper's end-of-year economics summary, and you've decided that you
    want to show a number of charts to demonstrate how different stocks have performed over the course of the last
    year. You have already decided that you want to show the price of n different stocks, all at the same k points
    of the year. A simple chart of one stock's price would draw lines between the points (0, p_0), (1, p_1), ...,
    (k - 1, p_k - 1), where p_i is the price of the stock at the i-th point in time. In order to save space, you
    have invented the concept of an overlaid chart. An overlaid chart is the combination of one or more simple
    charts, and shows the prices of multiple stocks (simply drawing a line for each one). In order to avoid
    confusion between the stocks shown in a chart, the lines in an overlaid chart may not cross or touch. Given a
    list of the prices of n stocks at each of k time points, you need to determine the minimum number of overlaid
    charts required to show all of the stocks' prices.

Input: The first line contains two integers n and k -- the number of stocks and the number of points in the year
    which are common for all of them. Each of the next n lines contains k integers. The i-th of those i lines
    contains the prices of the i-th stock at the corresponding k points in the year.

Constraints: 1 <= n <= 100; 1 <= k <= 25. All the stock prices are between 0 and 1000000.

Output: A single integer -- the minimum number of overlaid charts to visualize all the stock price data you have.
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


def min_charts(stock_data):
    num_stocks = len(stock_data)
    graph = [[] for _ in range(num_stocks * 2 + 2)]
    graph[0] += range(1, num_stocks + 1)
    for i in range(num_stocks - 1):
        for j in range(i + 1, num_stocks):
            if all([x > y for x, y in zip(stock_data[i], stock_data[j])]):
                graph[j + 1].append(i + 1 + num_stocks)
            elif all([x < y for x, y in zip(stock_data[i], stock_data[j])]):
                graph[i + 1].append(j + 1 + num_stocks)
    for j in range(num_stocks):
        graph[j + 1 + num_stocks].append(len(graph) - 1)
    flowgraph = transform_data(graph)
    max_flow(flowgraph, 0, num_stocks * 2 + 1)
    reachable_nodes = set()
    for i, edge in enumerate(flowgraph.edges):
        if edge.flow == 1 and edge.u in range(1, 1 + num_stocks):
            reachable_nodes.add(edge.v)
    return num_stocks - len(reachable_nodes)


if __name__ == '__main__':
    n, k = map(int, input().split())
    stock_data = [list(map(int, input().split())) for i in range(n)]
    result = min_charts(stock_data)
    print(result)