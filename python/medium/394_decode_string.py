class Solution:
    def decodeString(self, s: str) -> str:
        stack = [[1, []]]
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                buf = []
                while s[i] != "[":
                    buf.append(s[i])
                    i += 1
                stack.append([int(''.join(buf)), []])
                i += 1
            elif char == "]":
                n, seq = stack.pop()
                stack[-1][1] += seq * n
                i += 1
            else:
                stack[-1][1].append(char)
                i += 1

        return "".join(stack[0][1])
