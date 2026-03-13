import math
class Solution(object):
    def minNumberOfSeconds(self, h, times):
        low=1
        base=times[0]
        high=base*(h*(h+1))//2
        ans=high
        while low<=high:
            mid=(low+high)//2
            total=0
            for i in times:
                z=mid/i
                total+=(math.sqrt(1+8*z)-1)//2
            if total>=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans