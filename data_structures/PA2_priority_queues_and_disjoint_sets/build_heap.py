# python3

# 1. Convert array into heap
# Task: Convert a given array of integers into a min-heap using only O(n) swaps.
# Input: The first line contains a single integer n. The next line contains n space-separated integers a_i.
# Constraints: 1 <= n <= 100000; 0 <= i, j <= n - 1; 0 <= a_0, a_1, ..., a_n-1 <= 10^9. All a_i are distinct.
# Output: The first line should contain a single integer m -- the total number of swap operations used to convert
#     the array into a min-heap, satisfying the condition 0 <= m <= 4n. The next m lines should contain the swap
#     operations, with each swap described by two integers i, j -- the 0-based indices of the elements swapped.


def sift_down(i, data, swaps):
    minindex = i
    leftchild = 2 * i + 1
    if leftchild < len(data) and data[leftchild] < data[minindex]:
        minindex = leftchild
    rightchild = 2 * i + 2
    if rightchild < len(data) and data[rightchild] < data[minindex]:
        minindex = rightchild
    if i != minindex:
        data[i], data[minindex] = data[minindex], data[i]
        swaps.append((i, minindex))
        sift_down(minindex, data, swaps)


def generate_swaps(data):
    n = len(data)
    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, data, swaps)
    return swaps


if __name__ == '__main__':
    n = int(input())
    data = [int(s) for s in input().split()]
    swaps = generate_swaps(data)
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])
