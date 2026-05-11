class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums:
            k=i
            while k//10>0:
                ans.append(k//10)
                k=k%10
            ans.append(k)
        return ans
        