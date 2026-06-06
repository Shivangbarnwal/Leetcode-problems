class Solution(object):
    def rob(self, nums):
        n=len(nums)-1
        def robber(n,nums):
            n=len(nums)
            pre2=0
            pre1=nums[0]
            for i in range(1,n):
                cur=max(nums[i]+pre2,pre1)
                pre2=pre1
                pre1=cur
            return pre1
        if len(nums)==1:
            return nums[0]
        return max(robber(n-1,nums[1:]),robber(n-1,nums[:n]))