class Solution(object):
    def maxProfit(self, prices):
        profit=0
        cost=prices[0]
        for i in range(1,len(prices)):
            cost=min(cost,prices[i])
            profit=max(profit,prices[i]-cost)
        return profit