# python3
from sys import stdin

import itertools
import numpy as np


########################

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def select_pivot_element(a, used_rows, used_columns):
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    if a[pivot_element.row][pivot_element.column] == 0:
        for row in range(len(a)):
            for col in range(len(a[0])):
                if not used_rows[pivot_element.row] and not used_columns[pivot_element.column] and a[row][col] != 0:
                    pivot_element = Position(row, col)
                    return pivot_element
    return pivot_element


def swap_lines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] =\
        used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column


def process_pivot_element(a, b, pivot_element):
    pivot_value = a[pivot_element.row][pivot_element.column]
    if pivot_value not in (0, 1):
        for col in range(len(b)):
            a[pivot_element.row][col] /= pivot_value
        b[pivot_element.row] /= pivot_value
    for row in range(len(a)):
        if row != pivot_element.row:
            multiplier = a[row][pivot_element.column]
            if multiplier != 0:
                for col in range(len(b)):
                    a[row][col] -= multiplier * a[pivot_element.row][col]
                b[row] -= multiplier * b[pivot_element.row]


def mark_pivot_element_used(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def solve_equation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = select_pivot_element(a, used_rows, used_columns)
        swap_lines(a, b, used_rows, pivot_element)
        process_pivot_element(a, b, pivot_element)
        mark_pivot_element_used(pivot_element, used_rows, used_columns)
    print(a)
    return b

########################
  

def satisfies_inequalities(solution, A, b, indices):
    A_rows = A[indices]
    b_rows = b[indices]
    if not np.all(np.dot(A_rows, solution) <= b_rows):
        return False
    return True


def calculate_pleasure(solution, c):
    return np.dot(solution, c)


def solve_diet_problem(n, m, A, b, c):
    ineq_matrix = -np.identity(m)
    ineq_vector = [0 for _ in range(m)]
    A_ext = np.vstack([np.array(A), ineq_matrix])
    b_ext = np.array(b + ineq_vector)
    ineq_indices = list(itertools.combinations(range(n + m), m))
    candidate_solutions = []
    for i, index_set in enumerate(ineq_indices):
        A_rows = A_ext[list(index_set)]
        b_rows = b_ext[list(index_set)]
        equation = Equation(A_rows, b_rows)
        solution = np.array(solve_equation(equation))
        other_indices = list(set(range(n + m)) - set(index_set))
        if satisfies_inequalities(solution, A_ext, b_ext, other_indices):
            candidate_solutions.append(solution)
    if len(candidate_solutions) == 0:
        return -1, None
    max_pleasure = float('-inf')
    max_idx = None
    for i, solution in enumerate(candidate_solutions):
        pleasure = calculate_pleasure(solution, c)
        if pleasure > max_pleasure:
            max_pleasure = pleasure
            max_idx = i
    if np.sum(candidate_solutions[max_idx]) > 10 ** 9:
        return 1, None
    return 0, candidate_solutions[max_idx]


n, m = 1, 3
A = [[0, 0, 1]]
b = [3]
c = [1, 1, 1]

#n, m = list(map(int, stdin.readline().split()))
#A = []
#for i in range(n):
#    A += [list(map(int, stdin.readline().split()))]
#b = list(map(int, stdin.readline().split()))
#c = list(map(int, stdin.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, b, c)

if anst == -1:
    print("No solution")
if anst == 0:  
    print("Bounded solution")
    print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
    
