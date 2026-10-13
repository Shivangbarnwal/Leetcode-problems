class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        k=sorted([i**2 for i in nums])
        i=0
        j=len(nums)-1
        ma=0
        while i<j:
            ma+=(k[j]-k[i])
            j-=1
            i+=1
        if i==j:
            ma+=k[j]
        return ma