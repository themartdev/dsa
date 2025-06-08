class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        end, count = float('-inf'), 0
        intervals.sort(key=lambda x: x[1])
        for start, e in intervals:
            if start >= end:
                end = e
            else:
                count += 1
        return count

# -
#  -
#   -
#    -
# ----
#     ----

# build adjacency matrix of intervals
# sort by number of edges
# while there are still nodes with more than 2 edges:
#   - delete the node with the most edges
# efficient?? building the graph is O(n^2)...

# can we do something with the interval edges?
# or is there a mathematical rule/principle we can use?
