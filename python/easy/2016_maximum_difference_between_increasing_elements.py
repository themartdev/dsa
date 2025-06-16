class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        max_profit = -1
        l = 0
        for i in range(len(nums)):
            if nums[i] < nums[l]:
                l = i
            if nums[i] > nums[l]:
                max_profit = max(max_profit, nums[i] - nums[l])
        return max_profit
