class Solution(object):
    def maxProfit(self, prices):
        profit=0
        mini=prices[0]
        
        for i in range(1,len(prices)):
            cost=prices[i]-mini
            profit=max(profit,cost)
            mini=min(mini,prices[i])
        return profit