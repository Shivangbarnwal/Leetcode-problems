from collections import defaultdict
class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dis = float('inf')
        mpp=defaultdict(int)
        for i in range(len(nums)):
            k=int(str(nums[i]))
            if k in mpp:
                dis=min(dis,abs(mpp[k]-i))
            
            mpp[int(str(nums[i])[::-1])]=i
        if dis==float('inf'):
            return -1
        return dis
        