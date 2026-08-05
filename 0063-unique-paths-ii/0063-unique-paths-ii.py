class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*(n) for _ in range(m)]
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return 0
        dp[0][0]=1
        def rec(m,n):
            if m<0 or n<0:
                return 0
            if dp[m][n]!=-1:
                return dp[m][n]
            if grid[m][n]==1:
                dp[m][n]=0
                return 0
            top,left=0,0
            if m>0:
                top=rec(m-1,n)
            if n>0:
                left=rec(m,n-1)
            dp[m][n]=top+left
            return dp[m][n]
        return rec(m-1,n-1)