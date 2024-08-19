from typing import List


# 10

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        buf = []

        def backtrack(total: int, start: int):
            if total < 0:
                return
            elif total == 0:
                ans.append(list(buf))
            else:
                prev = None
                for i in range(start, len(candidates)):
                    if candidates[i] != prev:
                        buf.append(candidates[i])
                        backtrack(total - candidates[i], i + 1)
                        buf.pop()
                        prev = candidates[i]

        backtrack(target, 0)
        return ans
