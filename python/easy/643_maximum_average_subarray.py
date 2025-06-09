class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_value = 0
        for i in range(k):
            current_value += nums[i]

        max_val = current_value
        for j in range(k, len(nums)):
            current_value -= nums[j - k]
            current_value += nums[j]
            max_val = max(max_val, current_value)
        return max_val / k
