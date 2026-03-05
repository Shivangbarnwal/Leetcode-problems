class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        pre=[1]*n
        suf=[1]*n
        for i in range(n-1):
            pre[i+1]*=nums[i]*pre[i]
            suf[-i-2]*=nums[-i-1]*suf[-i-1]
        
        for j in range(n):
            pre[j]*=suf[j]
        return pre

        