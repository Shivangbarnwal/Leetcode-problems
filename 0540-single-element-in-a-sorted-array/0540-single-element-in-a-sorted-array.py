class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor=-1
        for i in nums:
            if xor==-1:
                xor=i
            else:
                xor^=i
        return xor
        