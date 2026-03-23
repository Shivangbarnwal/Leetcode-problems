class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        dp=[[(0,0) for _ in range(m)] for _ in range(n)]
        
        
        dp[0][0]=(grid[0][0],grid[0][0])
        for j in range(1,m):
            prev_max, prev_min = dp[0][j-1]
            val = grid[0][j]
            dp[0][j] = (prev_max * val, prev_min * val)
        for i in range(1, n):
            prev_max, prev_min = dp[i-1][0]
            val = grid[i][0]
            dp[i][0] = (prev_max * val, prev_min * val)
        for i in range(1,n):
            for j in range(1,m):
                num1ma,num1mi=dp[i-1][j]
                num2ma,num2mi=dp[i][j-1]
                maxi=max(num1ma,num2ma)*grid[i][j]
                mini=min(num1mi,num2mi)*grid[i][j]
                if mini>maxi:
                    maxi,mini=mini,maxi
                dp[i][j]=(maxi,mini)
        ans= max(dp[-1][-1][0],-1)
        if ans<0:
            return ans
        else:
            return ans  %(10**9+7)
        