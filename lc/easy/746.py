class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # dp is the cost of arriving at step i
        dp = [0 for _ in range(len(cost) + 1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        print(dp)
        return dp[len(cost)]

# [1, 100, 1, 1, 1, 100]

# [1, 100, 1]
# [1, 1, x]
