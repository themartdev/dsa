OPENING_BRACKETS = {'(', '{', '['}
CLOSING_BRACKETS = {')', '}', ']'}


def map_to_opening(char: str):
    if char == ']':
        return '['
    if char == '}':
        return '{'
    if char == ')':
        return '('


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in OPENING_BRACKETS:
                stack.append(char)
            elif char in CLOSING_BRACKETS:
                if len(stack) == 0 or stack[-1] != map_to_opening(char):
                    return False
                stack.pop()

        return len(stack) == 0
