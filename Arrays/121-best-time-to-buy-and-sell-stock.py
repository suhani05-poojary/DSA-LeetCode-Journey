class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        max_profit=0
        for price in prices:
            if(price<buy):
                buy=price
            profit=price-buy
            if(profit>max_profit):
                max_profit=profit 
        return max_profit               
