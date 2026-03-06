class Solution(object):
    def maxProduct(self, nums):
        minprod=nums[0]
        maxprod=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            cur=nums[i]
            if cur<0:
                minprod,maxprod=maxprod,minprod
            maxprod=max(cur,maxprod*cur)
            minprod=min(cur,minprod*cur)
            ans=max(ans,maxprod)
        return ans
        