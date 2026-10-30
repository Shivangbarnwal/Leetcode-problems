from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp=defaultdict(int)
        left=0
        maxi=0
        cur=0
        for right in range(len(s)):
            mpp[s[right]]+=1
            cur+=1
            while mpp[s[right]]>1:
                mpp[s[left]]-=1
                left+=1
                cur-=1
            maxi=max(maxi,cur)
        return maxi