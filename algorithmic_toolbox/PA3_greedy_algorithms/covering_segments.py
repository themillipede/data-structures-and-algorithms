# Uses python3
import sys
from collections import namedtuple

# 4. Collecting signatures
# Task: Given a set of n segments {[a_0, b_0], [a_1, b_1], ..., [a_(n-1), b_(n-1)]}
# with integer coordinates on a line, find the minimum number m of points such that
# each segment contains at least one point.
# Constraints: 1 <= n <= 100; 0 <= a_i <= b_i <= 10^9 for all 0 <= i <= n

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
