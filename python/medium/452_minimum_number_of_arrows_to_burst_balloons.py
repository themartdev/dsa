class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 1
        prev = points[0][1]
        for s, e in points[1:]:
            if s > prev:
                count += 1
                prev = e
        return count

# -
#   --
# -----
#    ---
