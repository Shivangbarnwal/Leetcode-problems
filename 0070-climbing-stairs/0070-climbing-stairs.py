class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+1)
        
        def ways(n):
            if n<=1:
                return 1
            if dp[n]!=-1:
                return dp[n]
            else:
                dp[n]=ways(n-1)+ways(n-2)
                return dp[n]
        return ways(n)


        