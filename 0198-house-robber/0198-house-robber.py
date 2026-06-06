class Solution(object):
    def rob(self, nums):
        n=len(nums)
        dp=[-1]*(n)
        def rob(n,nums):
            if n<0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            
            else:
                dp[n]=max(nums[n]+rob(n-2,nums),rob(n-1,nums))
                return dp[n]
        return rob(n-1,nums) 