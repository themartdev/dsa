class Solution:
    def coloredCells(self, n: int) -> int:
        curr = 1
        for i in range(1, n):
            curr += 4 * i
        return curr

# 1, 5, 13, 25
