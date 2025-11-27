class Solution(object):
    def maxSubarraySum(self, nums, k):
        maxi=-sys.maxsize
        n=len(nums)
        prefixSum=0
        ksum=[sys.maxsize//2]*k
        ksum[k-1]=0
        for i in range(n):
            prefixSum+=nums[i]
            maxi=max(maxi,prefixSum-ksum[i%k])
            ksum[i%k]=min(ksum[i%k],prefixSum)
        return maxi
        

        