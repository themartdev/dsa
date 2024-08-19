from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        buf: List[int] = []

        def backtrack(curr: int, start: int):
            if curr == 0:
                ans.append(list(buf))
            if curr <= 0:
                return
            for i in range(start, len(candidates)):
                buf.append(candidates[i])
                backtrack(curr - candidates[i], i)
                buf.pop()

        backtrack(target, 0)
        return ans
