class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        buf = []
        for char in s:
            if char == " ":
                if buf:
                    stack.append("".join(buf))
                    buf = []
            else:
                buf.append(char)
        if buf:
            stack.append("".join(buf))
        stack.reverse()
        return " ".join(stack)
