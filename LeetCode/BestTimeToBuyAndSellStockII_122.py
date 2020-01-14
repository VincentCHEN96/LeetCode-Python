class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0

        if prices:
            for i in range(0, (len(prices) - 1)):
                if prices[i] < prices[i + 1]:
                    max_profit += (prices[i + 1] - prices[i])

        return max_profit
