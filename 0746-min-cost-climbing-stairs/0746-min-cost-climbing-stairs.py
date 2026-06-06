class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        dp=[-1]*(n+1)
        def climb(cost,n):
            if dp[n]!=-1:
                return dp[n]
            elif n in [0,1]:
                dp[n]=0
                return dp[n]
            else:
                dp[n]=min(cost[n-1]+climb(cost,n-1),cost[n-2]+climb(cost,n-2))
                return dp[n]
        return climb(cost,n)
        