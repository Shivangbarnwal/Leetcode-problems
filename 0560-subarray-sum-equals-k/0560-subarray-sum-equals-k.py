from collections import defaultdict
class Solution(object):
    def subarraySum(self, arr, k):
        mpp=defaultdict(int)
        presum=0
        mpp[0]=1
        cnt=0
        for i in arr:
            presum+=i
            
            remove=presum-k
            cnt+=mpp[remove]
            mpp[presum]+=1
        return cnt