import collections


class Solution:
    grid: list[list[str]]
    m: int
    n: int

    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.grid = grid
        self.m = m
        self.n = n
        g = []
        # Build graph
        for k in range(m * n):
            adj = []
            for coord in self.neighbors(self.to2d(k)):
                adj.append(coord)
            g.append(adj)

        # Now we have a graph, let's DFS and count islands
        visited = [False for _ in range(len(g))]
        count = 0
        print(g)

        for k in range(len(g)):
            coords = self.to2d(k)
            if grid[coords[0]][coords[1]] == "1" and not visited[k]:
                count += 1
                # BFS here
                queue = collections.deque()
                queue.append(k)
                visited[k] = True
                while len(queue) != 0:
                    node = queue.popleft()
                    for other in g[node]:
                        other_k = self.to1d(other)
                        if not visited[other_k]:
                            visited[other_k] = True
                            queue.append(other_k)
                print(visited)

        return count

    def neighbors(self, coords: tuple[int, int]) -> list[tuple[int, int]]:
        def test(point: tuple[int, int]) -> bool:
            if point[0] < 0 or point[0] > self.m - 1 or point[1] < 0 or point[1] > self.n - 1:
                return False
            return self.grid[point[0]][point[1]] == "1"

        i, j = coords
        res = []
        for candidate in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if test(candidate):
                res.append(candidate)
        return res

    def to1d(self, coords: tuple[int, int]) -> int:
        return (coords[0] * self.n) + coords[1]

    def to2d(self, k) -> tuple[int, int]:
        return k // self.n, k % self.n
