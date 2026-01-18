class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        maxi=nums[0]
        cursum=0
        for i in nums:
            cursum+=i
            maxi=max(maxi,cursum)
            if cursum<0:
                cursum=0
        return maxi
