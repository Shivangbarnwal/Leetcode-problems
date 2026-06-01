class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        c=0
        cost.sort(reverse=True)
        for i in range(len(cost)):
            if (i+1)%3!=0:
                c+=cost[i]
        return c