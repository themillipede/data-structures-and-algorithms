# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def get_parent(table):
    if table != parent[table]:
        parent[table] = get_parent(parent[table])
    return parent[table]

def merge(destination, source):
    global ans
    real_destination, real_source = get_parent(destination), get_parent(source)

    if real_destination == real_source:
        return False

    if rank[real_destination] > rank[real_source]:
        parent[real_source] = real_destination
        lines[real_destination] += lines[real_source]
        lines[real_source] = 0
        ans = max(ans, lines[real_destination])
    else:
        parent[real_destination] = real_source
        lines[real_source] += lines[real_destination]
        lines[real_destination] = 0
        ans = max(ans, lines[real_source])
        if rank[real_source] == rank[real_destination]:
            rank[real_source] += 1
    
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
