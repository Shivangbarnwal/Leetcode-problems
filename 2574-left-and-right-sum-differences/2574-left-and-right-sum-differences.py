class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=sum(nums)
        a=[]
        left=0
        for i in nums:
            s-=i
            a.append(abs(s-left))
            left+=i
        return a