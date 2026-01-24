class Solution(object):
    def minPairSum(self, nums):
        maxi=0
        nums.sort()
        for i in range(len(nums)//2):
            maxi=max(maxi,(nums[i]+nums[-i-1]))
        return maxi