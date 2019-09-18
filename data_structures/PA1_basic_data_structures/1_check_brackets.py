# python3

"""
1. Check brackets in the code

Introduction: The goal of this problem is to implement a feature for a text editor to find errors in the usage of
    brackets in code.

Task: Given a string that may contain brackets from the set []{}(), find the first unmatched closing bracket which
    either doesn't have an opening bracket before it, or closes the wrong opening bracket. If there are no such
    mistakes, then find the first unmatched opening bracket without the corresponding closing bracket after it. If
    there are no mistakes, then indicate that the usage of brackets is correct.

Input: A string S comprising big and small latin letters, digits, punctuation marks and brackets from the set []{}().

Constraints: The length of S is at least 1 and at most 10^5.

Output: If the code in S uses brackets correctly, output "Success". Otherwise, output the 1-based index of the first
    unmatched closing bracket if one exists. If not, output the 1-based index of the first unmatched opening bracket.
"""

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def find_mismatch(text):
    opening_brackets_stack = []
    mismatch_index = None
    for i, next in enumerate(text):
        if next in '([{':
            bracket = Bracket(next, i + 1)
            opening_brackets_stack.append(bracket)
        if next in ')]}':
            if opening_brackets_stack:
                prev = opening_brackets_stack.pop()
                if not prev.match(next):
                    mismatch_index = i + 1
                    break
            else:
                mismatch_index = i + 1
                break
    if not mismatch_index and opening_brackets_stack:
        mismatch_index = opening_brackets_stack[0].position
    return mismatch_index


if __name__ == "__main__":
    text = sys.stdin.read()
    result = find_mismatch(text)
    if not result:
        result = 'Success'
    print(result)
