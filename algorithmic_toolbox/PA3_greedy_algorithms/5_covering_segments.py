# Uses python3

"""
4. Collecting signatures

Introduction: You are responsible for collecting signatures from all tenants of a certain building. For each
    tenant, you know a period of time when he or she is at home. You would like to collect all signatures by
    visiting the building as few times as possible. The mathematical model for this problem is the following:
    you are given a set of segments on a line and your goal is to mark as few points on the line as possible
    so that each segment contains at least one marked point.

Task: Given a set of n segments {[a_0, b_0], [a_1, b_1], ..., [a_(n-1), b_(n-1)]} with integer coordinates on
    a line, find the minimum number m of points such that each segment contains at least one point. That is,
    find a set of integers X of the minimum size such that for any segment [a_i, b_i] there is a point x in X
    such that a_i <= x <= b_i.

Input: The first line contains the number of segments, n. Each of the following n lines contains two integers
    a_i and b_i (separated by a space) defining the coordinates of endpoints of the i-th segment.

Constraints: 1 <= n <= 100; 0 <= a_i <= b_i <= 10^9 for all 0 <= i < n.

Output: The minimum number of points, m, on the first line and the integer coordinates of m points (separated
    by spaces) on the second line. You can output the points in any order, and if there are many such sets of
    points, you can output any set. (There always exist a set of points of the minimum size such that all the
    coordinates of the points are integers.)
"""

import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    sorted_segments = sorted(segments)
    curr_end = sorted_segments[0].end
    for segment in sorted_segments[1:]:
        if segment.start <= curr_end:
            curr_end = min(curr_end, segment.end)
        else:
            points.append(curr_end)
            curr_end = segment.end
    points.append(curr_end)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
