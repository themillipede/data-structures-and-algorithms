# Uses python2

"""
6. Closest points

Introduction: The goal in this problem is to find the closest pair of points among the given n points.

Task: Given n points on a plane, find the smallest distance between a pair of two (different) points.

Input: The first line contains the number of points n. Each of the following n lines defines a point (x_i, y_i).

Constraints: 2 <= n <= 10^5; -10^9 <= x_i, y_i <= 10^9 are integers.

Output: The minimum distance. The absolute value of the difference between the answer of your program and the
    optimal value should be at most 10^-3.
"""

import sys
import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def min_dist(coords):
    if len(coords) == 1:
        return float('inf')
    if len(coords) == 2:
        return distance(coords[0], coords[1])
    mid_idx = len(coords) // 2
    left = coords[:mid_idx]
    right = coords[mid_idx:]
    min_left = min_dist(left)
    min_right = min_dist(right)
    d = min(min_left, min_right)
    mid_xcoord = (left[-1][0] + right[0][0]) / 2
    left_xlimit = mid_xcoord - d
    right_xlimit = mid_xcoord + d
    left_idx = len(left) - 1
    while left_idx > -1 and left[left_idx][0] > left_xlimit:
        left_idx -= 1
    left_col = left[left_idx + 1:]
    right_idx = 0
    while right_idx < len(right) and right[right_idx][0] < right_xlimit:
        right_idx += 1
    right_col = right[:right_idx]
    middle_col = sorted(left_col + right_col, key=lambda x: x[1])
    for i, item in enumerate(middle_col):
        for j in range(i + 1, i + 8):
            if len(middle_col) > j:
                dist = distance(middle_col[i], middle_col[j])
                if dist < d:
                    d = dist
    return d


def minimum_distance(x, y):
    coords = sorted(zip(x, y))
    return min_dist(coords)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
