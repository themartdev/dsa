from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()

        def backtrack(trace: list[int], curr: int, min_idx: int):
            if curr == target:
                out.append(trace)
                return

            if curr > target:
                return

            for i in range(min_idx, len(candidates)):
                if i > min_idx and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(trace + [candidates[i]], curr + candidates[i], i + 1)

        backtrack([], 0, 0)

        return out
