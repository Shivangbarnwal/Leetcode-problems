class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c=0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                c+=1
        if c>1 or (c==1 and nums[-1]>nums[0]):
            return False
        return True