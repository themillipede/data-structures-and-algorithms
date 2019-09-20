# python3

"""
1. Infer energy values of ingredients

Introduction: In this problem, you will apply Gaussian Elimination to infer the energy values of ingredients
    given a restaurant menu with calorie counts and ingredient lists provided for each item.

Task: You're looking at a restaurant menu which shows for each dish the list of ingredients with amounts and
    the estimated total energy value in calories. You would like to find out the energy values of individual
    ingredients (then you will be able to estimate the total energy values of your favorite dishes).

Input: The first line contains an integer n -- the number of dishes in the menu, and it so happens that the number
    of different ingredients is the same. Each of the next n lines contains a description a_1, a_2, ..., a_n, E of
    a single menu item, where a_i is the amount of the i-th ingredient in the dish, and E is the estimated total
    energy value of the dish. If the ingredient i is not used in the dish, the amount a_i will be specified as 0.
    Be aware that although the amount of any ingredient in any real menu would be positive, we will test that your
    algorithm works even for negative amounts a_i < 0.

Constraints: 0 <= n <= 20; -1000 <= a_i <= 1000.

Output: Output n real numbers -- the energy value of each ingredient. These numbers can be non-integer, so output
    them with at least 3 digits after the decimal point. The amounts and energy values are of course approximate,
    and the computations in real numbers on a computer are not always precise, so the numbers in your output will
    be considered correct if either the absolute or the relative error is less than 10^-2.

"""


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
    pivot.row = max(potential_pivot_rows, key=lambda row: abs(a[row][pivot.column]))  # Argmax: improves stability.
    if a[pivot.row][pivot.column] == 0:
        used_columns[pivot.column] = True
        pivot = None
    return pivot


def swap_lines(a, b, used_rows, pivot):
    a[pivot.column], a[pivot.row] = a[pivot.row], a[pivot.column]
    b[pivot.column], b[pivot.row] = b[pivot.row], b[pivot.column]
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


if __name__ == "__main__":
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    equation = Equation(a, b)
    solution = solve_equation(equation)
    size = len(solution)
    for row in range(size):
        print("%.20lf" % solution[row])
