# python3
from sys import stdin

# Splay tree implementation


class Vertex:
    def __init__(self, key, sum, left, right, parent):
        self.key = key
        self.sum = sum
        self.left = left
        self.right = right
        self.parent = parent


def update(v):
    """
    Update sum attribute of vertex v, to be equal to the sum
    of the keys of all vertices in the subtree rooted at v.
    :param v: Vertex
    :return: None
    """
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
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


# Makes splay of the given vertex and makes it the new root.
def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree, then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return next, root


def split(root, key):
    """
    Split tree rooted at root into two subtrees. If a node with key value key
    is in the tree, that node will be splayed to the root and the tree rooted
    at its left child will break off to become the second subtree. If no node
    with key value key is in the tree, the next highest value will be splayed
    to the root, and the tree rooted at its left child will break off. If the
    key value is higher than the key value of any node in the tree, the whole
    tree rooted at root will be returned, with no second subtree.
    """
    result, root = find(root, key)
    if result is None:
        return root, None
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

  
# Code that uses splay tree to solve the problem
                                    
root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def erase_using_successor(x):
    global root

    def get_successor(n):
        if n.right is not None:
            current = n.right
            while current is not None:
                if current.left is None:
                    break
                current = current.left
            return current
        p = n.parent
        while p is not None:
            if n != p.right:
                break
            n = p
            p = p.parent
        return p

    successor = get_successor(x)
    if successor is None:
        p = x.parent
        p.right = None
        x.parent = None
    else:
        splay(successor)
        splay(x)
        left = x.left
        right = x.right
        right.left = left
        left.parent = right
        root = right
        right.parent = None


def erase(x):
    global root
    if not search(x):
        return
    root = merge(root.left, root.right)
    if root:
        root.parent = None


def search(x):
    """
    Check whether or not integer x is contained within the set.
    :param x: Integer
    :return: True or False
    """
    global root
    result, root = find(root, x)
    if result and result.key == x:
        return True
    return False


def sum_keys(fr, to):
    global root
    left, middle = split(root, fr)
    middle, right = split(middle, to + 1)
    ans = 0
    if middle:
        ans = middle.sum
    root = merge(merge(left, middle), right)
    return ans


MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum_keys((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
