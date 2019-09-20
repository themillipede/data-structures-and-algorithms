# python3

"""
3. Advanced Problem: Advertisement budget allocation

Introduction: In this problem, you'll work for a big company that uses advertising to promote itself. You will
    need to determine whether it is possible to allocate advertising budget and satisfy all the constraints. You
    will learn how to reduce this problem to a particular type of Integer Linear Programming problem. Then you
    will design and implement an efficient algorithm to reduce this type of Integer Linear Programming to SAT.

Task: The marketing department of your big company has many sub-departments which control advertising on TV, radio,
    web search, contextual advertising, mobile advertising, etc. Each of them has prepared an advertising campaign
    plan, and of course you don't have enough budget to cover all of their proposals. You don't have enough time to
    go thoroughly through each sub-department's proposals and cut them, because you need to set the budget for the
    next year tomorrow. You decide that you will either approve or decline each of the proposals as a whole. There
    are a bunch of constraints you face. For example, your total advertising budget is limited. Also, you have some
    contracts with advertising agencies for some of the advertisement types that oblige you to spend at least some
    fixed budget on that kind of advertising, or you'll face huge penalties, so you'd better spend it. Also, there
    are different company policies that can be of the form that you spend at least 10% of your total advertising
    spend on mobile advertising to promote yourself in this new channel, or that you spend at least $1M a month on
    TV advertisement, so that people always remember your brand. All of these constraints can be rewritten as an
    Integer Linear Programming task: for each sub-department i, denote by x_i a boolean variable that corresponds
    to whether you will accept or decline the proposal of that sub-department. Then each constraint can be written
    as a linear inequality. You will be given the final Integer Linear Programming problem in the input, and you
    will need to reduce it to SAT. It is guaranteed that there will be at most 3 different variables with non-zero
    coefficients in each inequality of this Integer Linear Programming problem.

Input: The first line contains two integers n and m -- the number of inequalities and the number of variables. The
    next n lines contain the description of n x m matrix A with coefficients of inequalities (each of the n lines
    contains m integers, and at most 3 of them are non-zero), and the last line contains the description of the
    vector b (n integers) for the system of inequalities Ax <= b. You need to determine whether there exists a
    binary vector x satisfying all those inequalities.

Constraints: 1 <= n, m <= 500; -100 <= A_ij <= 100; -1000000 <= b_i <= 1000000.

Output: A boolean formula in the CNF form in a specific format. If it is possible to accept some of the proposals
    and decline all the others while satisfying all the constraints, the formula must be satisfiable. Otherwise,
    the formula must be unsatisfiable. The number of variables in the formula must not exceed 3000, and the number
    of clauses must not exceed 5000.

    On the first line, output integers C and V -- the number of clauses in the formula and the number of variables
    respectively. On each of the next C lines, output a description of a single clause. Each clause has the form
    (x_4 OR ~x_1 OR x_8). For a clause with k terms, output first those k terms and then the number 0 at the end
    ("4 -1 8 0" for the example above). Output each term as an integer. Output variables x_1, x_2, ..., x_V as
    numbers 1, 2, ..., V respectively, and negations of variables ~x_1, ~x_2, ..., ~x_V as numbers -1, -2, ..., -V
    respectively. Each number other than the last one in each line must be be a non-zero integer between -V and V,
    where V is the total number of variables specified in the first line of the output. Ensure that 1 <= C <= 5000
    and 1 <= V <= 3000. If there are many different formulas that satisfy the requirements above, you can output
    any one of them.
"""

import sys
import numpy as np
from itertools import product


def print_equisatisfiable_sat_formula(A):
    result = []
    for i, ineq in enumerate(A):
        non_zeros = [j for j, coef in enumerate(ineq) if coef != 0]
        coefs = [ineq[j] for j in non_zeros]
        for variable_assignment in product([0, 1], repeat=len(non_zeros)):
            idx_to_var = {idx: var for idx, var in zip(non_zeros, variable_assignment)}
            if not np.dot(np.array(coefs), np.array(variable_assignment)) <= b[i]:
                # Current assignment does not satisfy this inequality.
                result.append([-j - 1 if idx_to_var[j] == 1 else j + 1 for j in non_zeros])

    # If there are no clauses, add a single satisfiable clause.
    if len(result) == 0:
        result.append([1, -1])

    print("%s %s" % (len(result), m))
    for clause in result:
        print(" ".join([str(i) for i in clause]) + " 0")


if __name__ == "__main__":
    n, m = list(map(int, sys.stdin.readline().split()))
    A = []
    for i in range(n):
        A += [list(map(int, sys.stdin.readline().split()))]
    b = list(map(int, sys.stdin.readline().split()))
    print_equisatisfiable_sat_formula(A)
