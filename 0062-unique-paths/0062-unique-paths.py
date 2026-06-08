class Solution(object):
    def uniquePaths(self, m, n):
        dp=[[0 for i in range(n)] for j in range(m)]
        def paths(i,j):
            if dp[i][j]!=0:
                return dp[i][j]
            if i==0 and j==0:
                dp[i][j]=1
                return 1
            elif i==0:
                dp[i][j]=paths(i,j-1)
            elif j==0:
                dp[i][j]=paths(i-1,j)
            else:
                dp[i][j]=paths(i-1,j)+paths(i,j-1)
            return dp[i][j]
        return paths(m-1,n-1)