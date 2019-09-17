# python3

"""
3. Car fueling

Introduction: You are going to travel to another city that is located d miles away from your home city. You can
    travel at most m miles on a full tank and you start with a full tank. Along your way, there are gas stations
    at distances stop_1, stop_2, ..., stop_n from your home city. What is the minimum number of refills needed?

Input: The first line contains an integer d. The second line contains an integer m. The third line contains an
    integer n. Finally, the last line contains integers stop_1, stop_2, ..., stop_n.

Constraints: 1 <= d <= 10^5; 1 <= m <= 400; 1 <= n <= 300; 0 < stop_1 < stop_2 < ... < stop_n < m.

Output: Assuming that the distance between the cities is d miles, a car can travel at most m miles on a full tank,
    and there are gas stations at distances stop_1, stop_2, ..., stop_n along the way, output the minimum number
    of refills needed to reach the destination. Assume that the car starts with a full tank. If it is not possible
    to reach the destination, output -1.
"""

import sys


def compute_min_refills(end_position, tank_capacity, stops):
    stops = [0] + stops
    stop_num = 0
    num_refills = 0
    current_position = 0

    while current_position < end_position:
        max_position = current_position + tank_capacity
        if max_position >= end_position:
            return num_refills  # If we can reach the end we are done.

        if stop_num + 1 < len(stops):
            if stops[stop_num + 1] > max_position:
                return -1  # If we can't reach the next stop, we give up.
        elif end_position > max_position:
            return -1  # We're at the last stop; if we can't reach the end, we give up.

        # Determine next furthest stop.
        while stop_num < len(stops) - 1 and stops[stop_num + 1] <= max_position:
            stop_num += 1

        num_refills += 1
        current_position = stops[stop_num]

    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
