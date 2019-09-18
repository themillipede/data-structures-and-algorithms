# python3
import sys, threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order(self):
        self.result = []
        def in_order_traversal(root_index):
            if self.left[root_index] != -1:
                in_order_traversal(self.left[root_index])
            self.result.append(self.key[root_index])
            if self.right[root_index] != -1:
                in_order_traversal(self.right[root_index])
        in_order_traversal(0)
        return self.result

    def pre_order(self):
        self.result = []
        def pre_order_traversal(root_index):
            self.result.append(self.key[root_index])
            if self.left[root_index] != -1:
                pre_order_traversal(self.left[root_index])
            if self.right[root_index] != -1:
                pre_order_traversal(self.right[root_index])
        pre_order_traversal(0)
        return self.result

    def post_order(self):
        self.result = []
        def post_order_traversal(root_index):
            if self.left[root_index] != -1:
                post_order_traversal(self.left[root_index])
            if self.right[root_index] != -1:
                post_order_traversal(self.right[root_index])
            self.result.append(self.key[root_index])
        post_order_traversal(0)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))

threading.Thread(target=main).start()
