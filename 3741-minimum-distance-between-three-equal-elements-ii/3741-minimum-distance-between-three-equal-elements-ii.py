from collections import defaultdict
class Solution(object):
    
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check(mindis,arr):
            for i in range(len(arr)-2):
                mindis=min(mindis,2*(arr[i+2]-arr[i]))
            return mindis
        mpp=defaultdict(list)
        for j in range(len(nums)):
            mpp[nums[j]].append(j)
        mindis=float('inf')
        for k in mpp.keys():
            if len(mpp[k])>=3:
                mindis=check(mindis,mpp[k])
        if mindis==float('inf'):
            return -1
        else:
            return mindis