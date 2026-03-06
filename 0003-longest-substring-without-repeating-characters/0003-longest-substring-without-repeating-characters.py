class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        mpp={}
        maxlen=0
        for right in range(len(s)):
            if s[right] not in mpp.keys():
                mpp[s[right]]=right
            else:
                if left<=mpp[s[right]]:
                    left=mpp[s[right]]+1
                mpp[s[right]]=right
            maxlen=max(maxlen,right-left+1)
        return maxlen