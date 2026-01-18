class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        preprod=1
        for i in range(len(nums)):
            arr.append(preprod)
            preprod*=nums[i]
        suff=1
        for i in range(1,len(nums)+1):
            arr[-i]*=suff
            suff*=nums[-i]
        return arr
        