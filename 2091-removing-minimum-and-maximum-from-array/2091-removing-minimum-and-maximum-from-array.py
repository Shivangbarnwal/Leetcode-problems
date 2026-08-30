class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        fma,fmi=nums.index(max(nums)),nums.index(min(nums))
        mi,ma=min(fma,fmi)+1,max(fma,fmi)+1
        n=len(nums)
        return min(ma,n-mi+1, mi+n-ma+1)