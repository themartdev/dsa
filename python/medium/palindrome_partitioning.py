from typing import List


def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[l]:
            return False
        l += 1
        r -= 1
    return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def backtrack(groups: list[str], idx: int):
            if idx == len(s):
                out.append(groups)
                return

            for right in range(idx, len(s)):
                val = s[idx:right + 1]
                if is_palindrome(val):
                    backtrack(groups + [val], right + 1)

        backtrack([], 0)

        return out
