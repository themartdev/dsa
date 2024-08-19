from typing import List

# 1,2,2,3
# 1 -> 2,2,3
# 2 -> 1,2,3
# 2 -> 1,2,3

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums = list(set(nums))
        nums.sort()
        ans = []
        curr = []

        def backtrack(start: int):
            ans.append(list(curr))
            prev = None
            for i in range(start, len(nums)):
                if nums[i] == prev:
                    continue
                curr.append(nums[i])
                backtrack(i + 1)
                prev = curr.pop()

        backtrack(0)
        return ans
