from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        buf = []

        def backtrack(start: int):
            ans.append(list(buf))
            for i in range(start, len(nums)):
                buf.append(nums[i])
                backtrack(i + 1)
                buf.pop()

        backtrack(0)
        return ans
