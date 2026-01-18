class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        mpp={}
        for i in range(n):
            if nums[i] in mpp.keys():
                return i,mpp[nums[i]]
            mpp[target-nums[i]]=i
        