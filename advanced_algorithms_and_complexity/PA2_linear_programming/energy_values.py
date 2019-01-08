# python3

EPS = 1e-6
PRECISION = 20


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def read_equation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


def select_pivot(a, used_rows, used_columns):
    pivot = Position(0, 0)
    while used_rows[pivot.row]:
        pivot.row += 1
    while used_columns[pivot.column]:
        pivot.column += 1
    min_unused_row = pivot.row
    while a[pivot.row][pivot.column] == 0 and pivot.row + 1 < len(a):
        pivot.row += 1
        if a[pivot.row][pivot.column] == 0 and pivot.column + 1 < len(a[0]):
            pivot.column += 1
            pivot.row = min_unused_row
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
        for col in range(len(b)):
            a[pivot.row][col] /= pivot_value
        b[pivot.row] /= pivot_value
    for row in range(len(a)):
        if row != pivot.row:
            multiplier = a[row][pivot.column]
            for col in range(len(b)):
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
        swap_lines(a, b, used_rows, pivot)
        process_pivot(a, b, pivot)
        mark_pivot_used(pivot, used_rows, used_columns)
    return b


def print_column(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])


if __name__ == "__main__":
    equation = read_equation()
    solution = solve_equation(equation)
    print_column(solution)
    exit(0)
