# python3

"""
3. Merging tables

Introduction: The goal in this problem is to simulate a sequence of merge operations with tables in a database.

Task: There are n tables, numbered from 1 to n, stored in some database. They all share the same set of columns.
    Each table can contain either rows with real data or a symbolic link to another table. Initially, all tables
    contain data, and the i-th table has r_i rows. There will be m merge queries to perform, each one defined by
    a source table and a destination table. In the first merge operation, all of the data in the source must be
    copied to the destination. The data in the source must then be removed and replaced with a symbolic link to
    the destination. In all subsequent merges, all symbolic links in either the source or the destination should
    be traversed to reach the "true" source and destination, before performing merges in the same way. Each time
    a merge operation has concluded, print the maximum size among all n tables (where size is the number of rows
    in the table). If the table contains only a symbolic link, its size is considered to be 0.

Input: The first line contains two integers n and m -- the number of tables in the database and the number of
    merge queries to perform, respectively. The second line contains n integers r_i -- the number of rows in the
    i-th table. The following m lines describe merge queries. Each line contains two integers: destination_i and
    source_i -- the numbers of the tables to merge.

Constraints: 1 <= n, m <= 100000; 0 <= r_i <= 10000; 1 <= destination_i, source_i <= n.

Output: For each query print a line containing a single integer -- the maximum of the sizes of all tables after
    the corresponding operation.
"""

import sys


def get_parent(table):
    if table != parent[table]:
        parent[table] = get_parent(parent[table])  # "Path compression" so every path node will point to the root.
    return parent[table]


def merge(destination, source):
    global max_size
    real_destination, real_source = get_parent(destination), get_parent(source)

    if real_destination == real_source:
        return

    if rank[real_destination] > rank[real_source]:  # "Union by rank" to ensure tree depth increases by at most 1.
        parent[real_source] = real_destination
        lines[real_destination] += lines[real_source]
        lines[real_source] = 0
        max_size = max(max_size, lines[real_destination])
    else:
        parent[real_destination] = real_source
        lines[real_source] += lines[real_destination]
        lines[real_destination] = 0
        max_size = max(max_size, lines[real_source])
        if rank[real_source] == rank[real_destination]:
            rank[real_source] += 1
    return


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))
    rank = [1] * n
    parent = list(range(0, n))
    max_size = max(lines)

    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        merge(destination - 1, source - 1)
        print(max_size)
