class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nuke=[]
        for kim in nums:
            if kim in nuke:
                return kim
            else:
                nuke.append(kim)
                