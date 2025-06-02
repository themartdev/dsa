from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def dfs(trace: list[int], allowed: set[int]):
            if not allowed:
                out.append(list(trace))
                return

            for num in allowed:
                trace.append(num)
                new_allowed = set(allowed)
                new_allowed.remove(num)
                dfs(trace, new_allowed)
                trace.pop()

        dfs([], set(nums))

        return out
