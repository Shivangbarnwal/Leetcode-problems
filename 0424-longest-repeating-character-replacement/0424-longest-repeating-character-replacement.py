class Solution(object):
    def characterReplacement(self, s, k):
        mpp={}
        maxcount=0
        maxlen=0
        left=0
        for right in range(len(s)):
            if s[right] in mpp.keys():
                mpp[s[right]]+=1
            else:
                mpp[s[right]]=1
            maxcount=max(maxcount,mpp[s[right]])
            while (right-left+1)-maxcount>k:
                mpp[s[left]]-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen