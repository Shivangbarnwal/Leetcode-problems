class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        suma=0
        maxi=-float('inf')
        for i in range(n):
            suma+=nums[i]
            maxi=max(maxi,suma)
            if suma<0:
                suma=0
        return maxi