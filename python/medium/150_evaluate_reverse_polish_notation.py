from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                if token == '-':
                    stack.append(left - right)
                if token == '*':
                    stack.append(left * right)
                if token == '/':
                    stack.append(int(left / right))
            else:
                stack.append(int(token))

        return stack[0]


if __name__ == "__main__":
    print(int("-11"))
