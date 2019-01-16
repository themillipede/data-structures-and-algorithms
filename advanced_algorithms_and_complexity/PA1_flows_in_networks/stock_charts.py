# python3

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


class StockCharts:

    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for i in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def min_charts(self, stock_data):
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

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)


if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
