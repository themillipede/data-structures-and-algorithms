# python3
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


if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    result = None
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            bracket = Bracket(next, i + 1)
            opening_brackets_stack.append(bracket)
        if next == ')' or next == ']' or next == '}':
            if opening_brackets_stack:
                prev = opening_brackets_stack.pop()
                if not prev.match(next):
                    result = i + 1
                    break
            else:
                result = i + 1
                break
    if not result:
        result = opening_brackets_stack[0].position if opening_brackets_stack else 'Success'
    print(result)
