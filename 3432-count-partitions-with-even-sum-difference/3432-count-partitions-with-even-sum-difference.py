class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        suma=sum(nums)
        k=0
        nu=0
        for i in range(len(nums)-1):
            k+=nums[i]
            suma-=nums[i]
            if abs(suma-k)%2==0:
                nu+=1
        return nu