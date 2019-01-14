# python3

from itertools import product
import numpy as np

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))


def print_equisatisfiable_sat_formula():
    result = []
    for i, ineq in enumerate(A):
        non_zeros = [j for j, coef in enumerate(ineq) if coef != 0]
        for variable_assignment in product([0, 1], repeat=len(non_zeros)):
            idx_to_var = {idx: var for idx, var in zip(non_zeros, variable_assignment)}
            solution = [idx_to_var[k] if k in idx_to_var else 0 for k in range(len(ineq))]
            if not np.dot(np.array(ineq), np.array(solution)) <= b[i]:
                result.append([(-1) * ineq[j] if idx_to_var[j] == 1 else ineq[j] for j in non_zeros])
            else:
                result.append([ineq[j] for j in non_zeros])
    print("%s %s" % (len(result), len(b)))
    for clause in result:
        print(" ".join([str(i) for i in clause]) + " 0")


print_equisatisfiable_sat_formula()
