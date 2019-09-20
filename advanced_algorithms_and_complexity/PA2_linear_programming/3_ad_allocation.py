# python3

"""
3. Advanced Problem: Online advertisement allocation

Introduction: In this problem you will help an online advertising system to allocate the ad impressions in its
    advertising network so as to maximize revenue while satisfying all the advertisers' requirements.

Task: You have n clients, they are all advertisers, and each of them wants to show their ads to some number of
    internet users as specified in the contract (or more) next month. Your online advertising network has m
    placements overall on all the sites connected to the network. You know how many users each advertiser wants
    to reach, how many users will see each of the m ad placements next month, and how much each advertiser is
    willing to pay for a user seeing their ad through each particular ad placement (different placements can be
    on different sites attracting different types of users, and each advertiser is more interested in the
    visitors of some sites than the others). You can show different ads of different advertisers in the same ad
    placement throughout the next month or always show the same ad of the same advertiser, but the total number
    of users that will see some ad in that placement is estimated and fixed. You want to maximize your total
    revenue which is the sum of amounts each advertiser will pay you for all the users who have seen their ads.

Input: You are given the ad allocation problem reduced to a linear programming problem of the form Ax <= b,
    x >= 0, SUM[i=1->q](c_i * x_i) -> max, where A is a matrix p x q, b is a vector of length p, c is a vector
    of length q, and x is the unknown vector of length q.

    The first line of the input contains integers p and q -- the number of inequalities in the system and the
    number of variables respectively. The next p + 1 lines contain the coefficients of the linear inequalities
    in the standard form Ax <= b. I.e. The i-th of the next p lines contains q integers A_i1, A_i2, ..., A_iq,
    and the next line after those contains p integers b_1, b_2, ..., b_p. These lines describe p inequalities
    of the form (A_i1 * x_1) + (A_i2 * x_2) + ... + (A_iq * x_q) <= b_i. The last line of the input contains q
    integers -- the coefficients c_i of the objective SUM[i=1->q](c_i * x_i) -> max.

Constraints: 1 <= n, m <= 100; -100 <= A_ij <= 100; -1000000 <= b_i <= 1000000; -100 <= c_i <= 100.

Output: If there is no allocation that satisfies all the requirements, output "No solution". If you can get as
    much revenue as you want despite all the requirements, output "Infinity". If the maximum possible revenue
    is bounded, output two lines. On the first line, output "Bounded solution". On the second line, output q
    real numbers -- the optimal values of the vector x (recall that x = x_ij is how many users will see the ad
    of advertiser i through the placement j, but we changed the numbering of variables to x_1, x_2, ..., x_q).
    Output all the numbers with at least 15 digits after the decimal point. Your solution will be accepted if
    all the inequalities are satisfied and the answer has absolute error of at most 10^-3.
"""

from sys import stdin

EPS = 1e-4


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


# Takes an int "n" that defines how many total inequality equations there are.
# Takes an int "m" that defines how many total variables there are.
# Takes a list of lists "a" of size n x m that contains the inequalities.
# Takes a list "b" of size n of the maximums of each inequality.
# Takes a list "c" that represents the optimization function to maximize.
# For example:
# x + y - 3z <= 10
# -5x + 10y <= 50
# 3x - 2y -4z <= 9
# Maximize: x + 6y -3z
# n, m = 3, 3
# a = [[1, 1, -3], [-5, 10, 0], [3, -2, -4]]
# b = [10, 50, 9]
# c = [1, 6, -3]


# A tableau of size (m + n + 1) x (n + 1) is created. Each inequality is placed in a row in the tableau, and a
# slack variable is added to each inequality. Slack variables are added to inequalities to transform them into
# equalities. In the example above, the tableau would look as follows for the standard (non-two-phase) format:
# [ 1,  1, -3, 1, 0, 0, 10]
# [-5, 10,  0, 0, 1, 0, 50]
# [ 3, -2, -4, 0, 0, 1,  9]
# [-1, -6,  3, 0, 0, 0,  0]

def create_tableau(a, b, c, n, phase_one_optimization):
    tableau = []
    phase_one_row = [0] * (len(c) + n + 2)
    # For phase one optimisation in a the two-phase Simplex method, any inequalities that have a solution less than
    # zero will be flipped (for example: 2x -3y <= -10 --> -2x + 3y <= 10). The corresponding slack variable in the
    # tableau will take the value -1, to account for the flip in sign. The two-phase approach will occur ONLY if an
    # optimal solution was not initially found.
    for i in range(n):
        if phase_one_optimization and b[i] < 0:
            slack_variables = [0] * n
            slack_variables[i] = -1.0
            tableau_row = [-1 * x for x in a[i]] + slack_variables + [-1 * b[i]]
            tableau.append(tableau_row)
            phase_one_row = [a + b for a, b in zip(phase_one_row, tableau_row)]
        else:
            slack_variables = [0] * n
            slack_variables[i] = 1.0
            tableau_row = a[i] + slack_variables + [b[i]]
            tableau.append(tableau_row)
    final_row = [-1 * x for x in c] + [0] * n + [0]
    tableau.append(final_row)
    return tableau, phase_one_row


# Bland's Rule will be used for selecting the pivot element:
# 1. Choose the leftmost column that is negative.
# 2. Among the rows, choose the one with the lowest ratio between the right-hand side of the tableau (value b)
#    and the column coefficient where the coefficient is greater than zero. If the minimum ratio is shared by
#    several rows, choose the row with the lowest column variable (basic variable) in it.
# For (2), the algorithm doesn't just take the minimum ratio, because the special case of multiple minima must
# be taken into account. Additionally, Bland's rule calls for the lowest-numbered basic variable, which is not
# the same as the lowest index. For this, the algorithm keeps track of the basic variable in list slack_rows.

def select_pivot_element(a, m, slack_rows, phase_one_optimization, phase_one_row):
    pivot_element = Position(0, 0)
    no_solution = False
    if phase_one_optimization:
        pivot_element.column = phase_one_row.index(max(phase_one_row[:-1]))
    else:  # Choose minimum based on first negative smallest index.
        pivot_element.column = a[len(a)-1][:-1].index(min(a[len(a)-1][:-1]))
    ratios = []
    if pivot_element.column is not None:
        for r in range(len(a)-1):
            if a[r][pivot_element.column] > 0:
                ratios.append(abs(a[r][-1] / a[r][pivot_element.column]))
            else:
                ratios.append(float("inf"))
        if all(i == float("inf") for i in ratios):
            no_solution = True
        row_min = min(ratios)
        row_min_indices = [i for i,x in enumerate(ratios) if x == row_min]
        # take into account the case of equal minima in rows. According to Bland's rule, choose least variable
        if len(row_min_indices) > 1:
            least_variable = []
            for j in row_min_indices:
                least_variable.append(slack_rows[j])
            pivot_element.row = slack_rows.index(min(least_variable))
        else:
            pivot_element.row = row_min_indices[0]
    else:
        no_solution = True
    return no_solution, pivot_element


# Process Pivot has been optimized to insert the value 0 in the pivot element column. This helps ensure that
# within the tableau the reduction to zero is always clear and not approximated with the epsilon functions.

def process_pivot_element(a,pivot_element, phase_one_optimization, phase_one_row):
    pri_mult = a[pivot_element.row][pivot_element.column]  # Primary multiplier from pivot element.
    a[pivot_element.row] = [n / pri_mult for n in a[pivot_element.row]]  # Make primary element have a value of 1.
    a[pivot_element.row][pivot_element.column] = 1.0
    for i in range(len(a)):
        if i != pivot_element.row:
            sec_mult = a[i][pivot_element.column]  # Secondary multiplier from row being updated.
            pri_row = [j * sec_mult for j in a[pivot_element.row]]
            a[i]= [a - b for a, b in zip(a[i], pri_row)]
            a[i][pivot_element.column] = 0
    if phase_one_optimization:
        sec_mult = phase_one_row[pivot_element.column]  # Secondary multiplier from row being updated.
        pri_row = [j * sec_mult for j in a[pivot_element.row]]
        phase_one_row = [a - b for a, b in zip(phase_one_row, pri_row)]
        phase_one_row[pivot_element.column] = 0
    return a, phase_one_row


# Solves a linear programming inequality use a tableau via the Simplex method.
# The algorithm will first attempt to solve the tableau assuming a basic feasible solution has been provided.
# If the tableau provided by the first attempt leads to an invalid solution, meaning one of the inequalities
# is violated by one of the values from the initial optimal values set, then the algorithm will create a new
# tableau and proceed to a two-phase Simplex method approach.

def solve_equation(a, b, c, n, m):
    if all(i <= 0 for i in c) and all(i >= 0 for i in b):
        return [0] * m
    tableau, phase_one_row = create_tableau(a, b, c, n, False)
    ans, phase_one_answer = solve_tableau(tableau, a, b, m, n, False, phase_one_row)
    # break immediately if the tableau reduced to
    if ans == [-1] or ans == [float("inf")]:
        return ans
    invalid_answer = valid_answer(ans, a, b, m, n)
    # Proceed to a two-phase simplex approach if one of the variables
    # in the optimal solution violates an inequality equation
    if invalid_answer:
        tableau, phase_one_row = create_tableau(a, b, c, n, True)
        ans, phase_one_answer = solve_tableau(tableau, a, b, m, n, True, phase_one_row)
        phase_one_answer_invalid = valid_answer(phase_one_answer, a, b, m, n)
        if ans == [-1] or ans == [float("inf")]:
            return ans
        invalid_answer = valid_answer(ans, a, b, m, n)
    if invalid_answer:
        if not phase_one_answer_invalid:
            return phase_one_answer
        else:
            return [-1]
    return ans


def valid_answer(ans, a, b, m, n):
    invalid_answer = False
    for i in range(n):
      valid_ans = 0
      for j in range(m):
          valid_ans += a[i][j] * ans[j]
      if epsilon_greater_than(valid_ans, b[i]):
          invalid_answer = True
    if not all(epsilon_greater_than_equal_to(i, 0) for i in ans):
      invalid_answer = True
    return invalid_answer


def solve_tableau(tableau, a, b, m, n, phase_one_optimization, phase_one_row):
    slack_rows = list(range(m,n+m))
    phase_one_complete = False
    phase_one_answer = [0] * m
    while (phase_one_optimization or
           not all(epsilon_greater_than_equal_to(i, 0) for i in tableau[len(tableau)-1][:-1])):
        if phase_one_optimization and all(epsilon_less_than_equal_to(k, 0) for k in phase_one_row[:-1]):
            phase_one_optimization = False
            phase_one_complete = True
            phase_one_answer = determine_answer(tableau, slack_rows)
            if all(epsilon_greater_than_equal_to(i, 0) for i in tableau[len(tableau)-1][:-1]):
                break
        no_solution, pivot_element = select_pivot_element(
            tableau, m, slack_rows, phase_one_optimization, phase_one_row
        )
        if no_solution:
            if phase_one_complete:
                return [-1], phase_one_answer
            else:
                return [float("inf")], phase_one_answer
        slack_rows[pivot_element.row] = pivot_element.column
        tableau, phase_one_row = process_pivot_element(
            tableau, pivot_element, phase_one_optimization, phase_one_row
        )
    return determine_answer(tableau, slack_rows), phase_one_answer


def determine_answer(tableau, slack):
    ans = [0] * m
    for i in range(n+m):
        if i < m and i in slack:
            index = slack.index(i)
            ans[i] = tableau[index][-1]
        elif i not in slack and tableau[-1][i] == 0:
            for j in range(n-1):
                if tableau[j][i] > 0:
                    return [-1]
        elif i < m:
            ans[i] = 0
    return ans


# Measure equality or inequality of two real numbers through an epsilon value EPS.

def epsilon_greater_than(a, b):
    return (a > b) and not isclose(a, b)


def epsilon_greater_than_equal_to(a, b):
    return (a > b) or isclose(a, b)


def epsilon_less_than(a, b):
    return (a < b) and not isclose(a, b)


def epsilon_less_than_equal_to(a, b):
    return (a < b) or isclose(a, b)


def isclose(a, b):
    return abs(a - b) <= EPS


def print_column(column):
    size = len(column)
    if size == 1 and column[0] == -1:
        print("No solution")
    elif size == 1 and column[0] == float("inf"):
        print("Infinity")
    else:
        print("Bounded solution")
        print(' '.join(list(map(lambda x: '%.18f' % x, column))))


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for row in range(n):
        a.append(list(map(float, input().split())))
    b = list(map(float, input().split()))
    c = list(map(float, input().split()))
    solution = solve_equation(a, b, c, n, m)
    print_column(solution)
