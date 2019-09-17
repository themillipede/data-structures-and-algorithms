# Uses python3

"""
5. Organizing a lottery

Introduction: You are organizing an online lottery. To play, a participant bets on a single integer. You then
    draw several ranges of consecutive integers at random. A participant's payoff then is proportional to the
    number of ranges that contain the participant's number, minus the number of ranges that do not contain it.
    You need an efficient algorithm for computing the payoffs for all participants. A naive way to do this is
    to simply scan, for all participants, the list of all ranges. However, you have thousands of participants
    and thousands of ranges, so you cannot afford a slow naive algorithm.

Task: You are given a set of points on a line and a set of segments on a line. Compute, for each point, the
    number of segments that contain this point.

Input: The first line contains two non-negative integers s and p defining the number of segments and the number
    of points on a line, respectively. The next s lines contain two integers a_i and b_i, which define the i-th
    segment [a_i, b_i]. The next line contains p integers defining points x_1, x_2, ..., x_p.

Constraints: 1 <= s, p <= 50000; -10^8 <= a_i <= b_i <= 10^8 for all 0 <= i < s; -10^8 <= x_j <= 10^8 for all
    0 <= j < p.

Output: p non-negative integers k_0, k_1, ..., k_(p-1) where k_i is the number of segments that contain x_i.
"""

import sys


def fast_count_segments(starts, ends, points):
    count = [0] * len(points)  # Record the number of segments for each point.

    labelled_positions = (
        [(s, 'l') for s in starts] +
        [(e, 'r') for e in ends] +
        [(p, 'p', i) for i, p in enumerate(points)]
    )
    # There's no need to retain order, as it doesn't matter which segment each start and end belongs to:
    # any start indicates an increment of 1 in segment coverage, and any end indicates a decrement of 1.
    labelled_positions.sort(key=lambda x: (x[0], x[1]))
    num_segments = 0
    for position in labelled_positions:
        if position[1] == 'l':
            num_segments += 1
        elif position[1] == 'r':
            num_segments -= 1
        elif position[1] == 'p':
            count[position[2]] = num_segments  # Exploits alphabetical order of l, p, and r.

    return count


def naive_count_segments(starts, ends, points):
    count = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                count[i] += 1
    return count


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    count = fast_count_segments(starts, ends, points)
    for x in count:
        print(x, end=' ')
