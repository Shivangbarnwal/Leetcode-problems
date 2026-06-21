from collections import defaultdict
class Solution(object):
    def maxIceCream(self, arr, coins):
        mpp=defaultdict(int)
        for i in arr:
            mpp[i]+=1
        ans=[]
        for i in sorted(mpp.keys()):
            ans.extend([i]*mpp[i])
        num=0
        i=0
        while i<len(arr) and coins>=ans[i]:
            num+=1
            coins-=ans[i]
            i+=1
        return num
        
        