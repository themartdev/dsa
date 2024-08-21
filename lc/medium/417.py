import collections


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        atlantic, pacific = [[False for _ in range(n)] for _ in range(m)], [[False for _ in range(n)] for _ in range(m)]
        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific[i][j] = True
                    pacific_queue.append((i, j))
                if i == m - 1 or j == n - 1:
                    atlantic[i][j] = True
                    atlantic_queue.append((i, j))

        self.flow_upwards(heights, atlantic_queue, atlantic)
        self.flow_upwards(heights, pacific_queue, pacific)

        ans = []
        for i in range(m):
            for j in range(n):
                if atlantic[i][j] and pacific[i][j]:
                    ans.append([i, j])
        return ans

    def flow_upwards(self, heights: list[list[int]], queue: collections.deque, bool_map: list[list[bool]]):
        while len(queue) > 0:
            i, j = queue.popleft()
            for coords in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= coords[0] < len(heights) and 0 <= coords[1] < len(heights[0]) and heights[coords[0]][
                    coords[1]] >= heights[i][j] and not bool_map[coords[0]][coords[1]]:
                    bool_map[coords[0]][coords[1]] = True
                    queue.append(coords)
