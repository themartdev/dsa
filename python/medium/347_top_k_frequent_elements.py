from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        a = list(freq.items())
        a.sort(key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], a[:k]))
