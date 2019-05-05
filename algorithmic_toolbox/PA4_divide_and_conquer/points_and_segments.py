# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    labelled_positions = (
        [(s, 'l') for s in starts] +
        [(e, 'r') for e in ends] +
        [(p, 'p', i) for i, p in enumerate(points)]
    )
    labelled_positions.sort(key=lambda x: (x[0], x[1]))
    num_segments = 0
    for position in labelled_positions:
        if position[1] == 'l':
            num_segments += 1
        elif position[1] == 'r':
            num_segments -= 1
        elif position[1] == 'p':
            cnt[position[2]] = num_segments

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
