class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        dp[0]=0
        def iter(n):
            if dp[n]!=-1:
                return dp[n]
            if n<0:
                return 0
            dp[n]=max(iter(n-1),iter(n-2)+nums[n-1])
            return dp[n]
        return iter(len(nums))