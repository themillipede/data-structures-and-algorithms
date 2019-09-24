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


def min_dist(coordinates):
    if len(coordinates) == 1:
        return float('inf')
    if len(coordinates) == 2:
        return distance(coordinates[0], coordinates[1])
    mid_idx = len(coordinates) // 2
    left = coordinates[:mid_idx]
    right = coordinates[mid_idx:]

    min_left = min_dist(left)  # Minimum distance between two points in the left half.
    min_right = min_dist(right)  # Minimum distance between two points in the right half.

    d = min(min_left, min_right)  # Minimum distance before having checked the column of width 2d in the middle.
    mid_xcoord = (left[-1][0] + right[0][0]) / 2  # x-coordinate of the vertical line splitting points in two.
    left_xlimit = mid_xcoord - d  # Leftmost x-coordinate for points that should be checked over the boundary.
    right_xlimit = mid_xcoord + d  # Rightmost x-coordinate for points that should be checked over the boundary.

    left_idx = len(left) - 1  # Index of the rightmost point in the left half.
    while left_idx > -1 and left[left_idx][0] > left_xlimit:
        left_idx -= 1
    left_col = left[left_idx + 1:]  # All points in the left central column of width d.

    right_idx = 0  # Index of the leftmost point in the right half.
    while right_idx < len(right) and right[right_idx][0] < right_xlimit:
        right_idx += 1
    right_col = right[:right_idx]  # All points in the right central column of width d.

    middle_col = sorted(left_col + right_col, key=lambda x: x[1])  # Sort middle column points by y-coordinate.
    for i, item in enumerate(middle_col):
        for j in range(i + 1, i + 8):  # If |i - j| > 7, the distance between points p_i and p_j must be greater
            if len(middle_col) > j:    # than d, so we only need to check the nearest 7 points vertically.
                dist = distance(middle_col[i], middle_col[j])
                if dist < d:  # If the distance between two points in different halves is smaller than the
                    d = dist  # smallest distance currently recorded, update the smallest distance.
    return d


def minimum_distance(x, y):
    coordinates = sorted(zip(x, y))
    return min_dist(coordinates)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
