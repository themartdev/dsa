from typing import List


def get_neighbors(grid: List[List[int]], i: int, j: int):
    coords = (
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    )
    for coord in coords:
        if 0 <= coord[0] <= len(grid) - 1 and 0 <= coord[1] <= len(grid[0]) - 1:
            yield coord


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue: list[(int, int)] = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        ticks = 0
        while len(queue) > 0:
            ticks += 1
            next_queue: list[(int, int)] = []
            while len(queue) > 0:
                i, j = queue.pop()
                for n_i, n_j in get_neighbors(grid, i, j):
                    if grid[n_i][n_j] == 1:
                        fresh -= 1
                        next_queue.append((n_i, n_j))
                        grid[n_i][n_j] = 2

            queue = next_queue

        if fresh != 0:
            return -1
        return ticks - 1
