from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])

        up, down = 0, m - 1
        # Bin search row
        while 1:
            if up > down:
                return False
            i = (up + down) // 2
            lower_bound, higher_bound = matrix[i][0], matrix[i][n - 1]
            if target < lower_bound:
                down = i - 1
            elif target > higher_bound:
                up = i + 1
            else:
                break

        # Bin search col
        row = matrix[(up + down) // 2]
        left, right = 0, len(row) - 1
        while left <= right:
            i = (left + right) // 2
            val = row[i]
            if val == target:
                return True
            if val < target:
                left = i + 1
            elif val > target:
                right = i - 1
        return False
