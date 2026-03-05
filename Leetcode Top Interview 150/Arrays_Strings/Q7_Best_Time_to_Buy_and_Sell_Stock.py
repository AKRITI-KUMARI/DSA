class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        buyingPrice = float('inf')
        for i in range(len(prices)):
            if(prices[i] > buyingPrice):
                profit = max(profit, prices[i]-buyingPrice)
            else:
                buyingPrice = prices[i]
        return profit
  