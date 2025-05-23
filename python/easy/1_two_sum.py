from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            diffs[diff] = i

        for i in range(len(nums)):
            val = nums[i]
            if val in diffs and diffs[val] != i:
                return [diffs[val], i]
        raise RuntimeError()
