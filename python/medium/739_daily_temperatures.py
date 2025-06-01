import heapq
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        heap = []
        for i in range(len(temperatures)):
            while len(heap) > 0 and heap[0][0] < temperatures[i]:
                _, pop_i = heapq.heappop(heap)
                ans[pop_i] = i - pop_i
            heapq.heappush(heap, (temperatures[i], i))
        return ans
