class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        def rec(m,n):
            if m == 0 and n == 0:
                return grid[0][0]
            if m<0 or n<0:
                return float('inf')
            if dp[m][n]!=-1:
                return dp[m][n]
            top=rec(m-1,n)
            left=rec(m,n-1)
            dp[m][n]=min(rec(m-1,n),rec(m,n-1))+grid[m][n]
            return dp[m][n]
        return rec(m-1,n-1)
            