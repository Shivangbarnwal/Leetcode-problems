from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mpp=defaultdict(int)
        for i in nums:
            mpp[i]+=1
        bucket=[[] for i in range(len(nums)+1)]
        for num,freq in mpp.items():
            bucket[freq].append(num)
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res)==k:
                    return res
       
        
        