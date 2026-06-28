class Solution(object):
    def maxSum(self, nums, k, nul):
        """
        :type nums: List[int]
        :type k: int
        :type mul: int
        :rtype: int
        """
        nums.sort(reverse=True)
        suma=0
        for i in range(min(len(nums),k)):
            suma+=max(nums[i]*nul,nums[i])
            nul-=1
        return suma