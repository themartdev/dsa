from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        trace = set()

        def backtrack(pos: tuple[int, int] | None, k: int) -> bool:
            if k == len(word) - 1:
                return True
            candidates = self.neighbors(pos[0], pos[1], board) if pos else self.all_coords(board)

            for next_i, next_j in candidates:
                if board[next_i][next_j] == word[k + 1] and not (next_i, next_j) in trace:
                    trace.add((next_i, next_j))
                    res = backtrack((next_i, next_j), k + 1)
                    trace.remove((next_i, next_j))
                    if res:
                        return True
            return False

        return backtrack(None, -1)

    def all_coords(self, board: List[List[str]]) -> List[tuple[int, int]]:
        for i in range(len(board)):
            for j in range(len(board[0])):
                yield i, j

    def neighbors(self, i: int, j: int, board: List[List[str]]) -> List[tuple[int, int]]:
        res = []
        if len(board) == 0:
            return res
        if i > 0:
            res.append((i - 1, j))
        if i < len(board) - 1:
            res.append((i + 1, j))
        if j > 0:
            res.append((i, j - 1))
        if j < len(board[0]) - 1:
            res.append((i, j + 1))

        print(f"neighbors of ({i},{j}): {res}")
        return res
