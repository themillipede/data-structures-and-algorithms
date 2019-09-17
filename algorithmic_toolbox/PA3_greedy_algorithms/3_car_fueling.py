# python3
import sys


def compute_min_refills(end_position, tank_capacity, stops):
    stops = [0] + stops
    stop_num = 0
    num_refills = 0
    current_position = 0

    while current_position < end_position:
        max_position = current_position + tank_capacity
        if max_position >= end_position:
            return num_refills  # if we can reach the end we are done

        if stop_num + 1 < len(stops):
            if stops[stop_num + 1] > max_position:
                return -1  # if we can't reach the next stop, we give up
        elif end_position > max_position:
            return -1  # we're at the last stop, if we can't reach the end, we give up

        # determine next farthest stop
        while stop_num < len(stops) - 1 and stops[stop_num + 1] <= max_position:
            stop_num += 1

        num_refills += 1
        current_position = stops[stop_num]

    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
