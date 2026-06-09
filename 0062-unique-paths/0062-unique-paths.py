class Solution(object):
    def uniquePaths(self, m, n):
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        dp[0]=[1]*n
        for i in range(1,m):
            for j in range(n):
                if i==0:
                    dp[i][j]=dp[i][j-1]
                elif j==0:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]