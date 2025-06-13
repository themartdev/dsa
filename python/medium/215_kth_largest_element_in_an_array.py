from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        curr = 0
        for _ in range(k):
            curr = heappop(nums)
        return -curr
