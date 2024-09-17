class Solution:
    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> list[list[str]]:
        res = []

        def backtrack(s2: str, curr: list[str]):
            print(f"backtrack: {s2}, {curr}")
            if len(s2) < 1:
                res.append(curr)
                return
            for i in range(len(s2)):
                sub = s2[:i + 1]
                if self.is_palindrome(sub):
                    new = curr.copy()
                    new.append(sub)
                    backtrack(s2[i + 1:], new)

        backtrack(s, [])

        return res
