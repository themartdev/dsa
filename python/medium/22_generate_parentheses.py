from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def backtrack(curr: str, n_open: int, n_to_open: int):
            if n_to_open == 0 and n_open == 0:
                out.append(curr)
            else:
                if n_to_open > 0:
                    backtrack(curr + "(", n_open + 1, n_to_open - 1)
                if n_open > 0:
                    backtrack(curr + ")", n_open - 1, n_to_open)

        backtrack("", 0, n)

        return out
