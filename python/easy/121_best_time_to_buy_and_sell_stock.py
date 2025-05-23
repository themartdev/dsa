from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        for i in range(len(prices)):
            if prices[i] < prices[l]:
                l = i
            max_profit = max(max_profit, prices[i] - prices[l])
        return max_profit
