class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*(n) for i in range(m)]
        dp[0]=[1]*(n)
        for i in range(m):
            dp[i][0]=1
        
        def iter(m,n):
            if dp[m][n]!=-1:
                return dp[m][n]
            left,top=0,0
            if m>0:
                top=iter(m-1,n)
            if n>0:
                left=iter(m,n-1)
            dp[m][n]=left+top
            return dp[m][n]
        return iter(m-1,n-1)
        