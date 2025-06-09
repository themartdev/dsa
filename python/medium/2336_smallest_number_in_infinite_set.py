import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.min_val = 1

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            self.min_val += 1
            return self.min_val - 1

    def addBack(self, num: int) -> None:
        if self.min_val > num and num not in self.heap:
            heapq.heappush(self.heap, num)
