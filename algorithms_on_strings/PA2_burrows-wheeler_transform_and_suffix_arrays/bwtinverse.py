# python3
import sys


def InverseBWT(bwt):
    last = [(val, i) for i, val in enumerate(bwt)]
    first = sorted(last)
    first_to_last = {f: l for f, l in zip(first, last)}
    next = first[0]
    result = ''
    for _ in range(len(bwt)):
        result += next[0]
        next = first_to_last[next]
    text = result[::-1]
    return text


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
