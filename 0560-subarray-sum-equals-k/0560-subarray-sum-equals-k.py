from collections import defaultdict
class Solution(object):
    def subarraySum(self, arr, k):
        mpp=defaultdict(int)
        count=0
        n=len(arr)
        cursum=0
        mpp[0]=1
        for i in range(n):
            cursum+=arr[i]
            
            remove=cursum-k
            count+=mpp[remove]
            mpp[cursum]+=1
        return count

