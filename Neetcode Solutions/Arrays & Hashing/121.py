# BEST TIME TO BUY AND SELL STOCK

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        low_price=prices[0]
        max_profit=0

        for i in range(len(prices)):
            low_price=min(low_price,prices[i])
            max_profit=max(max_profit,prices[i]-low_price)
        
        return max_profit
