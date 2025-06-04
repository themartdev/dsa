from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for outer_i in range(len(visited)):
            for outer_j in range(len(visited[0])):
                if visited[outer_i][outer_j] == 1:
                    continue
                if board[outer_i][outer_j] == "X":
                    visited[outer_i][outer_j] = 1
                    continue

                q = [(outer_i, outer_j)]
                visited[outer_i][outer_j] = 1
                edge_encountered = False
                batch = []
                while q:
                    i, j = q.pop()
                    batch.append((i, j))
                    if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                        edge_encountered = True
                    for ia, ja in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                        if 0 <= ia < len(board) and 0 <= ja < len(board[0]) and not visited[ia][ja] and board[ia][
                            ja] == "O":
                            visited[ia][ja] = 1
                            q.append((ia, ja))
                if not edge_encountered:
                    for i, j in batch:
                        board[i][j] = "X"
