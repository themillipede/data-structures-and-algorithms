# python3


def print_equisatisfiable_sat_formula():
    print("%s %s" % (m * 3 + n, n * 3))
    for vertex in range(1, n + 1):
        start = vertex * 3 - 2
        print("%s %s %s 0" % (start, start + 1, start + 2))
    for edge in edges:
        u = edge[0]
        v = edge[1]
        u_start = u * 3 - 2
        v_start = v * 3 - 2
        print("-%s -%s 0" % (u_start, v_start))
        print("-%s -%s 0" % (u_start + 1, v_start + 1))
        print("-%s -%s 0" % (u_start + 2, v_start + 2))


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    print_equisatisfiable_sat_formula()
