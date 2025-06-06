import math


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        vertical = [set() for _ in range(9)]
        horizontal = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        def get_square_set(i: int, j: int) -> set[int]:
            row = int(math.floor(i / 3))
            col = int(math.floor(j / 3))
            sq = row * 3 + col
            print(f"square {sq} for ({i},{j})")
            return square[sq]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                value = int(board[i][j])
                print(f"value ({i}, {j}) {value}")
                vertical_set = vertical[j]
                horizontal_set = horizontal[i]
                square_set = get_square_set(i, j)
                if value in vertical_set or value in horizontal_set or value in square_set:
                    return False
                else:
                    vertical_set.add(value)
                    horizontal_set.add(value)
                    square_set.add(value)
        return True
