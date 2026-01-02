class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-2):
            if nums[i]==nums[i+1] or nums[i]==nums[i+2]:
                return nums[i]
        
        if nums[0]==nums[-1] or nums[-1]==nums[-2]:
            return nums[-1]                