# python3
import sys
import itertools
import numpy as np


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def select_pivot(a, used_rows, used_columns):
    pivot = Position(0, 0)
    while used_columns[pivot.column]:
        pivot.column += 1
    potential_pivot_rows = [i for i in range(pivot.row, len(a)) if not used_rows[i]]
    pivot.row = max(potential_pivot_rows, key=lambda row: abs(a[row][pivot.column]))
    if a[pivot.row][pivot.column] == 0:
        used_columns[pivot.column] = True
        pivot = None
    return pivot


def swap_lines(a, b, used_rows, pivot):
    a[pivot.column], a[pivot.row] = a[pivot.row], a[pivot.column].copy()
    b[pivot.column], b[pivot.row] = b[pivot.row], b[pivot.column].copy()
    used_rows[pivot.column], used_rows[pivot.row] = used_rows[pivot.row], used_rows[pivot.column]
    pivot.row = pivot.column


def process_pivot(a, b, pivot):
    pivot_value = a[pivot.row][pivot.column]
    if pivot_value == 0:
        return
    if pivot_value != 1:
        for col in range(pivot.column, len(b)):
            a[pivot.row][col] /= pivot_value
        b[pivot.row] /= pivot_value
    for row in range(len(a)):
        if row != pivot.row:
            multiplier = a[row][pivot.column]
            for col in range(pivot.column, len(b)):
                a[row][col] -= multiplier * a[pivot.row][col]
            b[row] -= multiplier * b[pivot.row]


def mark_pivot_used(pivot, used_rows, used_columns):
    used_rows[pivot.row] = True
    used_columns[pivot.column] = True


def solve_equation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot = select_pivot(a, used_rows, used_columns)
        if not pivot:
            continue
        swap_lines(a, b, used_rows, pivot)
        process_pivot(a, b, pivot)
        mark_pivot_used(pivot, used_rows, used_columns)
    return b
  

def solve_diet_problem(n, m, A, b, c):
    A_ext = np.vstack([np.array(A), -np.identity(m), np.ones(m)]).astype(float)
    b_ext = np.array(b + [0] * m + [1e9]).astype(float)
    ineq_indices = list(itertools.combinations(range(n + m + 1), m))
    candidate_solutions = []
    for i, index_set in enumerate(ineq_indices):
        A_rows = A_ext[list(index_set)]
        b_rows = b_ext[list(index_set)]
        equation = Equation(A_rows, b_rows)
        solution = solve_equation(equation)
        if np.all(np.dot(A_ext, solution) <= b_ext + 10e-3):  # check if solution satisfies inequality
            candidate_solutions.append(solution)
    if len(candidate_solutions) == 0:
        return -1, None
    max_pleasure = float('-inf')
    max_idx = None
    for i, solution in enumerate(candidate_solutions):
        pleasure = np.dot(solution, c)
        if pleasure > max_pleasure:
            max_pleasure = pleasure
            max_idx = i
    if np.sum(candidate_solutions[max_idx]) >= 10**9:
        return 1, None
    return 0, candidate_solutions[max_idx]


if __name__ == "__main__":
    n, m = list(map(int, sys.stdin.readline().split()))
    A = []
    for i in range(n):
        A += [list(map(int, sys.stdin.readline().split()))]
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    anst, ansx = solve_diet_problem(n, m, A, b, c)
    if anst == -1:
        print("No solution")
    if anst == 0:
        print("Bounded solution")
        print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
    if anst == 1:
        print("Infinity")
