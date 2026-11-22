class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi=nums[0]
        cur=0
        for i in nums:
            cur+=i
            maxi=max(maxi,cur)
            if cur<0:
                cur=0
        return maxi