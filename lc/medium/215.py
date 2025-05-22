import random


def partition(nums: list[int], l: int, r: int) -> int:
    pivot = nums[r]
    i = l
    for j in range(l, r):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        random.shuffle(nums)
        target_i = len(nums) - k
        l, r = 0, len(nums) - 1
        while l < r:
            pivot_i = partition(nums, l, r)
            if pivot_i < target_i:
                l = pivot_i + 1
            elif pivot_i > target_i:
                r = pivot_i - 1
            else:
                break

        return nums[target_i]
