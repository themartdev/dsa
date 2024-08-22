class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    surrounded = True
                    current_group: list[(int, int)] = [(i, j)]
                    stack = [(i, j)]
                    visited[i][j] = True
                    while len(stack) > 0:
                        r, c = stack.pop()
                        if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                            surrounded = False
                        for rn, cn in ((r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)):
                            if 0 <= rn < m and 0 <= cn < n and board[rn][cn] == "O" and not visited[rn][cn]:
                                visited[rn][cn] = True
                                current_group.append((rn, cn))
                                stack.append((rn, cn))
                    if surrounded:
                        for r, c in current_group:
                            board[r][c] = "X"
