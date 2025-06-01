from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    n += 1
                    self.bfs(grid, i, j)

        return n

    def bfs(self, grid: list[list[str]], i: int, j: int):
        to_visit = [(i, j)]
        grid[i][j] = "0"
        while len(to_visit) > 0:
            i, j = to_visit.pop()
            for ia, ja in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ia < len(grid) and 0 <= ja < len(grid[0]) and grid[ia][ja] == "1":
                    grid[ia][ja] = "0"
                    to_visit.append((ia, ja))
