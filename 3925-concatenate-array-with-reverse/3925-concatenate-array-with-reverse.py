class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums[::-1])
        return nums