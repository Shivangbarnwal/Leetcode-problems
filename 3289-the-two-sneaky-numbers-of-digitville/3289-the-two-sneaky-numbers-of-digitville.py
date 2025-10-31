class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        l=[]
        for i in nums:
            if i>=len(nums):
                l.append(i)
            elif i in d.keys():
                l.append(i)
            else:
                d[i]=1
        return l
        