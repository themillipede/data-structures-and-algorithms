# python3

"""
2. Optimal diet problem

Introduction: In this problem, you will implement an algorithm for solving linear programming with only a few
    inequalities and apply it to determine the optimal diet.

Task: You want to optimize your diet: that is, make sure that your diet satisfies all of the recommendations of
    nutrition experts, but that you also get maximum pleasure from your food and drink. For each dish and drink
    you know all the nutrition facts, the cost of it, and an estimation of how much you like it. Your budget is
    limited, of course. The recommendations are of the form "the total number of calories consumed daily should
    be at least 1000" or "the amount of water drunk in litres should be at least twice the amount of food eaten
    in kilograms" etc. You optimize the total pleasure, which is the sum of the pleasure you get from consuming
    each particular dish or drink, which is proportional to the amount amount_i of that dish or drink consumed.

    The budget restrictions and nutrition recommendations can be converted into a system of linear inequalities
    of the form SUM[i=1->m](cost_i * amount_i) <= Budget, amount_i >= 1000 and amount_i - (2 * amount_j) >= 0,
    where amount_i is the amount of the i-th dish or drink consumed, cost_i is the cost of one item of the i-th
    dish or drink, and Budget is your total budget for the diet. You can only eat a non-negative amount of any
    item, so amount_i >= 0 for every i. The goal to maximize total pleasure is reduced to the linear objective
    SUM[i=1->m](amount_i * pleasure_i) -> max, where pleasure_i is the pleasure you get from consuming one unit
    of the i-th dish or drink (some dishes like fish oil you don't like at all, so pleasure_i can be negative).
    Combined, this becomes a linear programming problem, which you need to solve. It is guaranteed that in all
    test cases in this problem, if a solution is bounded, then amount_1 + amount_2 + ... + amount_m <= 10^9.

Input: The first line contains integers n and m -- the number of restrictions on your diet and the number of
    dishes and drinks respectively. The next n + 1 lines contain the coefficients of the linear inequalities
    in the standard form Ax <= b, where x = amount is the vector of length m with amounts of each ingredient,
    A is the n x m matrix with coefficients of inequalities, and b is the vector with the right-hand side of
    each inequality. Concretely, the i-th of the next n lines contains m integers A_i1, A_i2, ..., A_im, and
    the next line after those contains n integers b_1, b_2, ..., b_n. These lines describe n inequalities of
    the form (A_i1 * amount_1) + (A_i2 * amount_2) + ... + (A_im * amount_m) <= b_i. The last line of the
    input contains m integers -- the pleasure from consuming one item of each dish and drink
    pleasure_1, pleasure_2, ..., pleasure_m.

Constraints: 1 <= n, m <= 8; -100 <= A_ij <= 100; -1000000 <= b_i <= 1000000; -100 <= cost_i <= 100.

Output: If there is no diet that satisfies all the restrictions, output "No solution". If you can get as much
    pleasure as you want despite all the restrictions, output "Infinity". If the maximum possible total pleasure
    is bounded, output two lines. On the first line, output "Bounded solution". On the second line, output m real
    numbers -- the optimal amounts for each dish and drink. Output all the numbers with at least 15 digits after
    the decimal point.

    The amounts you output will be inserted into the inequalities, and all the inequalities will be checked. An
    inequality L <= R will be considered satisfied if L <= R + 10^-3. The total pleasure of your solution will
    be calculated and compared with the optimal value. Your output will be accepted if all the inequalities are
    satisfied and the total pleasure of your solution differs from the optimal value by at most 10^-3.
"""

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
  

# There are at most 8 inequalities (16 including the inequalities amount_i >= 0) with at most 8 variables; the
# optimal solution is always in a vertex of the polyhedron corresponding to the linear programming problem; at
# least m of the inequalities become equalities in each vertex of the polyhedron.
# If there are n regular inequalities, m variables, and m inequalities of the form amount_i >= 0, need to take
# each possible subset of size m out of all the n + m inequalities, solve the system of linear equations where
# each equation is one of the selected inequalities changed to equality, check whether this solution satisfies
# all the other inequalities, and finally select the solution with the largest value of the total pleasure out
# of those which satisfy all inequalities.

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
        if np.all(np.dot(A_ext, solution) <= b_ext + 10e-3):  # Check if solution satisfies inequality.
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
