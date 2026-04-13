class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        mindis=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                mindis=min(mindis,abs(i-start))
        return mindis