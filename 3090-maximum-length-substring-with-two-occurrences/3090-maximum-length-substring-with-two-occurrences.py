from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        mpp=defaultdict(int)
        left=0
        count=0
        for right in range(n):
            mpp[s[right]]+=1
            while mpp[s[right]]>2:
                mpp[s[left]]-=1
                left+=1
            count=max(count,right-left+1)
        return count