from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []

        def backtrack(chain: List[int], remaining: int, min_idx: int):
            if remaining == 0:
                out.append(chain)

            if remaining < 0:
                return

            for i in range(min_idx, len(candidates)):
                num = candidates[i]
                new_remaining = remaining - num
                new_chain = [x for x in chain]
                new_chain.append(num)
                backtrack(new_chain, new_remaining, i)

        backtrack([], target, 0)

        return out
