class Solution(object):
    def rob(self, nums):
        n=len(nums)
        dp=[-1]*(n+1)
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,n+1):
            dp[i]=max(nums[i-1]+dp[i-2],dp[i-1])
        return dp[n]