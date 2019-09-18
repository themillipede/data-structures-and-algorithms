# python3

"""
1. Convert array into heap

Introduction: In this problem you will convert an array of integers into a heap. This is the crucial step of the
    HeapSort algorithm. It has guaranteed worst-case running time of O(nlogn) as opposed to QuickSort's average
    running time of O(nlogn). QuickSort is usually used in practice because typically it is faster, but HeapSort
    is used for external sort when you need to sort huge files that don't fit into the memory of your computer.

Task: The first step of the HeapSort algorithm is to create a heap from the array you want to sort. Your task is
    to implement this first step and convert a given array of integers into a heap by applying a certain number
    of swaps to the array. The swap is an operation that exchanges elements a_i and a_j of an array a for some i
    and j. You will need to convert the array into a heap using only O(n) swaps. Use a min-heap, not a max-heap.

Input: The first line contains a single integer n. The next line contains n space-separated integers a_i.

Constraints: 1 <= n <= 100000; 0 <= i, j <= n - 1; 0 <= a_0, a_1, ..., a_(n-1) <= 10^9. All a_i are distinct.

Output: The first line should contain a single integer m -- the total number of swaps. The condition 0 <= m <= 4n
    must be satisfied. The next m lines should contain the swap operations used to convert the array into a heap.
    Each swap is described by a pair of integers i, j -- the 0-based indices of the elements swapped. Application
    of all the swaps in the specified order must convert the array into a heap.
"""


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
    for i in range(n // 2 - 1, -1, -1):  # Start with the deepest right-most parent and move up the "tree".
        sift_down(i, data, swaps)
    return swaps


if __name__ == '__main__':
    n = int(input())
    data = [int(s) for s in input().split()]
    swaps = generate_swaps(data)
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])
