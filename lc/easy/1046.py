import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones_inverted = [it * -1 for it in stones]
        heapq.heapify(stones_inverted)

        while len(stones_inverted) > 1:
            a = heapq.heappop(stones_inverted)
            b = heapq.heappop(stones_inverted)
            if a == b:
                continue
            else:
                a -= b
                heapq.heappush(stones_inverted, a)

        if len(stones_inverted) == 0:
            return 0

        return stones_inverted[0] * -1
