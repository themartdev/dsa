class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        res = curr = 0
        for delta in gain:
            curr += delta
            res = max(res, curr)
        return res
