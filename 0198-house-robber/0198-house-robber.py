class Solution(object):
    def rob(self, nums):
        n=len(nums)
        pre2=0
        pre1=nums[0]
        for i in range(1,n):
            cur=max(nums[i]+pre2,pre1)
            pre2=pre1
            pre1=cur
        return pre1