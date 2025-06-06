from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for _ in range(len(nums))]
        val = nums[0]
        for i in range(1, len(nums)):
            out[i] = val
            val *= nums[i]

        val = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            out[i] *= val
            val *= nums[i]
        return out


if __name__ == "__main__":
    for i in range(4, 0, -1):
        print(i)
