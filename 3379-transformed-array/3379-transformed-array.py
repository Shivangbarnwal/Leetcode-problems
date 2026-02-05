class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        n=len(nums)
        for i in range(n):
            arr.append(nums[(i+nums[i])%n])
        return arr
        