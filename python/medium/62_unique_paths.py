class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                total = 0
                if i > 0:
                    total += dp[i - 1][j]
                if j > 0:
                    total += dp[i][j - 1]
                dp[i][j] = total

        return dp[m - 1][n - 1]
