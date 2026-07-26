class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+2)
        dp[0]=0
        dp[1]=0
        for i in range(2,n+2):
            dp[i]=max(dp[i-1],nums[i-2]+dp[i-2])
        return dp[-1]