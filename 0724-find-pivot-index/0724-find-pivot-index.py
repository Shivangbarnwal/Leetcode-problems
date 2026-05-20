class Solution(object):
    def pivotIndex(self, nums):
        s=sum(nums)
        left=0
        for i in range(len(nums)):
            if i>0:
                left+=nums[i-1]
            s-=nums[i]
            if left==s:
                return i
        return -1