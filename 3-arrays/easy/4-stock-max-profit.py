# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            minimum = min(prices[i-1], minimum)
            profit = prices[i] - minimum
            max_profit = max(max_profit, profit)

        return max_profit
            