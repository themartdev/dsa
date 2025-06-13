class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        visited = [[0] * len(maze[0]) for _ in range(len(maze))]
        q = [entrance]
        next_q = []
        visited[entrance[0]][entrance[1]] = 1

        n = 1
        while q:
            for i, j in q:
                for ai, aj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if (0 <= ai < len(maze)
                            and 0 <= aj < len(maze[0])
                            and not visited[ai][aj]
                            and maze[ai][aj] == "."):
                        if ai == 0 or aj == 0 or ai == len(maze) - 1 or aj == len(maze[0]) - 1:
                            return n
                        else:
                            visited[ai][aj] = 1
                            next_q.append([ai, aj])

            n += 1
            q = next_q
            next_q = []
        return -1

# obviously a BFS graph problem
