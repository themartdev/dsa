class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = flipped = max_ones = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                while flipped == k:
                    if nums[left] == 0:
                        flipped -= 1
                        left += 1
                        break
                    left += 1
                flipped += 1
            max_ones = max(max_ones, right - left + 1)
        return max_ones
