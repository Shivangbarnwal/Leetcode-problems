class Solution(object):
    def maxRotateFunction(self, nums):
        init=0
        n=len(nums)
        for i in range(n):
            init+=nums[i]*i
        suma=sum(nums)
        maxi=init
        for j in range(1,n):
            init+=suma
            init-=n*nums[-j]
            maxi=max(maxi,init)
        return maxi