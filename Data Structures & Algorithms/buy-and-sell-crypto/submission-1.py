class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #using two pointers
        start =0
        end = 1
        #store max
        max_profit=0

        while end < len(prices):

            if prices[start] >= prices[end]:
                start = end
            else:
                profit = prices[end]-prices[start]
                max_profit = max(profit, max_profit)
            
            end+=1
        return max_profit