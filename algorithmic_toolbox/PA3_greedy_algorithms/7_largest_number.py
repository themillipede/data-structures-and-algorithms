# Uses python3

"""
6. Maximum salary

Introduction: At the end of a successful interview, your boss gives you a few pieces of paper with numbers on it
    and asks you to compose a larger number from these numbers. The resulting number is going to be your salary,
    so you are very interested in maximizing this number. How can you do this?

    In the lectures, we considered an algorithm for composing the largest number out of a set of single-digit
    numbers. Unfortunately, this algorithm only works in cases where the input consists of only single-digit
    numbers. For example, for an input consisting of two integers 23 and 3 (23 is not a single-digit number!)
    it returns 233, when the largest number is in fact 323. In other words, using the largest number from the
    input as the first number is not a safe move. Your goal in this problem is to construct an algorithm that
    works not only for single-digit numbers, but for arbitrary positive integers.

Task: Compose the largest number possible out of a set of integers.

Input: The first line contains an integer n. The second line contains integers a_1, a_2, ..., a_n.

Constraints: 1 <= n <= 100; 1 <= a_i <= 10^3 for all 1 <= i <= n.

Output: The largest number that can be composed out of a_1, a_2, ..., a_n.
"""

import sys


# First approach.
def largest_number(int_array):
    res = ""
    while int_array:
        max_digit = float('-inf')
        for digit in int_array:
            # Check whether int(str(digit) + str(max_digit))
            # is larger than int(str(max_digit) + str(digit)).
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        res += str(max_digit)
        int_array.remove(max_digit)
    return res


# Simpler alternative to the function directly below.
def is_greater_or_equal_simple(a, b):
    if b == float('-inf'):
        return True
    a = str(a)
    b = str(b)
    return int(a + b) >= int(b + a)


# More complicated than necessary.
def is_greater_or_equal(a, b):
    if b == float('-inf'):
        return True
    a = str(a)
    b = str(b)
    i = 0
    while i < max(len(a), len(b)) and a[i % len(a)] == b[i % len(b)]:
        i += 1
    return int(a[i % len(a)]) >= int(b[i % len(b)])


# Second approach.
def largest_number_alt(int_array):
    extended_nums = []
    ans = ""
    max_length = len(str(max(int_array))) + 1  # Consider numbers 141 and 14 to see why the "+1" is necessary.
    for num in int_array:
        ext_num = str(num) * max_length
        extended_nums.append((ext_num[:max_length], num))
    extended_nums.sort(reverse=True)
    for i in extended_nums:
        ans += str(i[1])
    return ans


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
