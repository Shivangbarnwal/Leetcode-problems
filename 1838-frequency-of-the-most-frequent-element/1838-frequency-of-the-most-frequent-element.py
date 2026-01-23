class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        suma=0
        n=len(nums)
        maxi=0
        left=0
        for right in range(n):
            suma+=nums[right]
            cost=nums[right]*(right-left+1)-suma
            while cost>k:
                suma-=nums[left]
                left+=1
                cost=nums[right]*(right-left+1)-suma
            maxi=max(maxi,right-left+1)
        return maxi