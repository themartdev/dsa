class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l = r = 0
        n = len(nums)
        c0 = mx = 0
        while r < n:
            if nums[r] == 0:
                c0 += 1
            while l < n and c0 == 2:
                if nums[l] == 0:
                    c0 -= 1
                l += 1
            mx = max(r - l, mx)
            r += 1
        return mx
