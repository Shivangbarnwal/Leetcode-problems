class Solution(object):
    def minimumTotal(self, t):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp=[]
        m=len(t)
        n=len(t[-1])
        for j in range(m):
            dp.append([0]*(len(t[j])))
        k=2
        dp[0][0]=t[0][0]
        for i in range(1,m):
            for j in range(k):
                left,right=float('inf'),float('inf')
                if j!=0:
                    left=dp[i-1][j-1]
                if j!=k-1:
                    right=dp[i-1][j]
                dp[i][j]=t[i][j]+min(left,right)
            k+=1
        return min(dp[-1])
                


        