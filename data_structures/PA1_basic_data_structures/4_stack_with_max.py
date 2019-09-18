# python3
import sys

# 4. Extending stack interface
# Task: Implement a stack supporting the operations Push(), Pop(), and Max().
# Input: The first line contains the number q of queries. Each of the following q lines specifies a query of one of
#     the following formats: push v, pop, or max.
# Constraints: 1 <= q <= 400000, 0 <= v <= 10000.
# Output: For each max query, output (on a separate line) the maximum value of the stack.


class StackWithMax:
    def __init__(self):
        self.main_stack = []
        self.aux_stack = []

    def push(self, a):
        self.main_stack.append(a)
        if not self.aux_stack or a >= self.aux_stack[-1]:
            self.aux_stack.append(a)

    def pop(self):
        if not self.main_stack:
            raise RuntimeError('Stack is empty')
        popped = self.main_stack.pop()
        if self.aux_stack and self.aux_stack[-1] == popped:
            self.aux_stack.pop()

    def max(self):
        if not self.main_stack:
            raise RuntimeError('Stack is empty')
        if self.aux_stack:
            return self.aux_stack[-1]


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
            raise RuntimeError('Invalid operation')
