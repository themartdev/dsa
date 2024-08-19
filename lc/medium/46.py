from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)
        ans = []
        buf = []

        def backtrack(depth: int):
            if len(buf) == len(nums):
                ans.append(list(buf))
                return
            for item in nums_set:
                print(f"Item {item}, buf {buf}, depth {depth}")
                if item not in buf:
                    buf.append(item)
                    backtrack(depth + 1)
                    buf.remove(item)

        backtrack(0)
        return ans
