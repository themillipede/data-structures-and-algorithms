# python3

import sys, threading
from collections import deque
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height_naive(self):
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height);
        return maxHeight;

    def compute_height(self):
        nodes = [[] for _ in range(len(self.n))]
        for i, node in enumerate(self.parent):
            if node == -1:
                root = i
            else:
                nodes[node].append(i)
        q = deque()
        q.append((root, 1))
        while q:
            node = q.popleft()
            node_number = node[0]
            node_height = node[1]
            for n in nodes[node_number]:
                q.append((n, node_height + 1))
        return node_height


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())


threading.Thread(target=main).start()
