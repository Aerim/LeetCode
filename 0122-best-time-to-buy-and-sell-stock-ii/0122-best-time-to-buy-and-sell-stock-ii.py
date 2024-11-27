class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_price = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)):
            if prices[i] > prev_price:
                max_profit += prices[i] - prev_price
                
            prev_price = prices[i]
            
        
        return max_profit
                