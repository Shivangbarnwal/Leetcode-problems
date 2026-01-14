class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        mpp={}
        maxi=0
        for right in range(len(s)):
            if s[right] in mpp.keys() and left<=mpp[s[right]]:
                left=mpp[s[right]]+1
            mpp[s[right]]=right
            maxi=max(maxi,right-left+1)
        return maxi