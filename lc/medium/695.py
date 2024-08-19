import collections


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        max_size = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    count = 0
                    q = collections.deque()
                    q.append((i, j))
                    visited[i][j] = True
                    while len(q) > 0:
                        ip, jp = q.popleft()
                        count += 1
                        for candidate in [(ip - 1, jp), (ip + 1, jp), (ip, jp - 1), (ip, jp + 1)]:
                            if 0 <= candidate[0] < m and 0 <= candidate[1] < n and grid[candidate[0]][candidate[1]] and not visited[candidate[0]][candidate[1]]:
                                visited[candidate[0]][candidate[1]] = True
                                q.append(candidate)
                    max_size = max(max_size, count)

        return max_size
