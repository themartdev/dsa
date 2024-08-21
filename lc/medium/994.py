class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # get initial rotten oranges
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
            print(queue)
            ticks += 1
            next_queue = []
            while len(queue) > 0:
                point = queue.pop()
                i, j = point
                for coord in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]) and grid[coord[0]][coord[1]] == 1:
                        fresh -= 1
                        next_queue.append(coord)
                        grid[coord[0]][coord[1]] = 2

            queue = next_queue
        return ticks - 1 if fresh == 0 else -1

# 2 1 1
# 1 1 0
# 0 1 1
