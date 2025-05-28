from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        out = []

        def backtrack(current: List[int], min_idx: int):
            out.append(current)

            if min_idx >= len(nums):
                return

            for i in range(min_idx, len(nums)):
                new_curr = [x for x in current]
                new_curr.append(nums[i])
                backtrack(new_curr, i + 1)

        backtrack([], 0)

        return out

# 0
# --- depth 1
# [0], min = 1
# 1
# 2