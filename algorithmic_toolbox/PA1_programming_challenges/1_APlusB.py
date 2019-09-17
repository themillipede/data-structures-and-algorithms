# python3

"""
1. Sum of two digits (SIMPLE PROBLEM TO SHOW SUBMISSION FORMAT)

Task: Compute the sum of two single digit numbers.

Input: Two integers a and b on the same line (separated by a space).

Constraints: 0 <= a, b <= 9.

Output: The sum of a and b.
"""


def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
