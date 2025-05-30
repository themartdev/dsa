from typing import List


def get_neighbors(grid: List[List[int]], i: int, j: int):
    coords = (
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    )
    for coord in coords:
        if 0 <= coord[0] <= len(grid) - 1 and 0 <= coord[1] <= len(grid[0]) - 1 and grid[coord[0]][coord[1]]:
            yield coord


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_size = max(max_size, self.dfs_island_size(grid, visited, i, j))
        return max_size

    def dfs_island_size(self, grid: List[List[int]], visited: List[List[int]], i: int, j: int) -> int:
        if visited[i][j] or not grid[i][j]:
            return 0
        stack = [(i, j)]
        total = 0
        while len(stack) != 0:
            curr = stack.pop()
            total += 1
            visited[curr[0]][curr[1]] = True
            for neighbor in get_neighbors(grid, curr[0], curr[1]):
                if not visited[neighbor[0]][neighbor[1]]:
                    visited[neighbor[0]][neighbor[1]] = 1
                    stack.append(neighbor)

        return total
