# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1

        return max_profit
