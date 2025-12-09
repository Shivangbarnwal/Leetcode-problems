class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        ans=[]
        for i in range(len(nums)):
            suma=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    suma+=1
            ans.append(suma)
        return ans
        