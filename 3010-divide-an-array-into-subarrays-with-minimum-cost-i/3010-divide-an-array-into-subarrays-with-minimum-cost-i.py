class Solution(object):
    def minimumCost(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        f=arr[0]
        arr.pop(0)
        arr.sort()
        return sum(arr[:2])+f