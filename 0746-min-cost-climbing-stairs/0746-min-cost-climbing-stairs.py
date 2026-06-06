class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        pre1,pre2=0,0
        for i in range(2,n+1):

            cur=min(cost[i-1]+pre1,cost[i-2]+pre2)
            pre2=pre1
            pre1=cur
        return pre1
        