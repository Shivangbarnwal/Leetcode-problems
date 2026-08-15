class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x=nums[0]
        n=len(nums)
        if nums==[0]*n:
            return 0
        for i in range(1,n):
            x^=nums[i]
        if x==0:
            return n-1
        else:
            return n