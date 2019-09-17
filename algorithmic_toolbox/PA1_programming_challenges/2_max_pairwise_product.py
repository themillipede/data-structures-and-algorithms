# python3

"""
2. Maximum pairwise product

Task: Find the maximum product of two distinct numbers in a sequence of non-negative integers. Concretely,
    given a sequence of non-negative integers a_1, ..., a_n, compute MAX[1 <= i < j <= n] (a_i * a_j).

Input: The first line contains an integer n. The next line contains n non-negative integers a_1, ..., a_n
    (separated by spaces).

Constraints: 2 <= n <= 2*10^5; 0 <= a_1, ..., a_n <= 2*10^5.

Output: The maximum pairwise product.
"""


# Naive, inefficient algorithm.
def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n - 1):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])
    return max_product


# More efficient algorithm.
def max_pairwise_product(numbers):
    n = len(numbers)
    index = 0
    for i in range(1, n):
        if numbers[i] > numbers[index]:
            index = i
    numbers[index], numbers[n - 1] = numbers[n - 1], numbers[index]
    index = 0
    for i in range(1, n - 1):
        if numbers[i] > numbers[index]:
            index = i
    return numbers[index] * numbers[n - 1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
