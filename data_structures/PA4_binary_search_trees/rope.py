# python3

import sys


class Vertex:
    def __init__(self, char, size, left, right, parent):
        self.char = char
        self.size = size
        self.left = left
        self.right = right
        self.parent = parent


def update(v):
    if v is None:
        return
    v.size = 1 + (v.left.size if v.left else 0) + (v.right.size if v.right else 0)
    if v.left:
        v.left.parent = v
    if v.right:
        v.right.parent = v


def small_rotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def big_rotation(v):
    if ((v.parent.left == v and v.parent.parent.left == v.parent)
    or (v.parent.right == v and v.parent.parent.right == v.parent)):
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    else:
        # Zig-zag
        small_rotation(v)
        small_rotation(v)


def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v


def find(root, size):
    s = root.left.size if root.left else 0
    if size == s + 1:
        return root
    elif size < s + 1:
        return find(root.left, size)
    elif size > s + 1:
        return find(root.right, size - s - 1)


def split(root, size):
    if size > root.size:
        return root, None
    result = find(root, size)
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return left, right


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


class Rope:
    def __init__(self, s):
        self.s = s

    def build_rope(self):
        root = Vertex(char=self.s[0], size=1, left=None, right=None, parent=None)
        for char in self.s[1:]:
            v = Vertex(char, 1 + root.size, left=root, right=None, parent=None)
            root.parent = v
            root = v
        self.s = root

    def in_order(self, node):
        if not node:
            return []
        return self.in_order(node.left) + [node] + self.in_order(node.right)

    def result(self):
        nodes = self.in_order(self.s)
        return "".join(n.char for n in nodes)

    def process(self, i, j, k):
        left, right = split(self.s, j + 2)
        left, middle = split(left, i + 1)
        right = merge(left, right)
        left, right = split(right, k + 1)
        middle = merge(left, middle)
        self.s = merge(middle, right)
                

rope = Rope(sys.stdin.readline().strip())
rope.build_rope()
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
