# python3
import sys


def BWT(text):
    rotations = [text[i:] + text[:i] for i in range(len(text), 0, -1)]
    rotations.sort()
    bwt = ''.join([string[-1] for string in rotations])
    return bwt


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
