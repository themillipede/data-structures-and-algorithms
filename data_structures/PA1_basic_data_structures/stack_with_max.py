# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__aux_stack = []

    def push(self, a):
        self.__stack.append(a)
        if not self.__aux_stack or a >= self.__aux_stack[-1]:
            self.__aux_stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        popped = self.__stack.pop()
        if self.__aux_stack and self.__aux_stack[-1] == popped:
            self.__aux_stack.pop()

    def max(self):
        assert(len(self.__stack))
        if self.__aux_stack:
            return self.__aux_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert(0)