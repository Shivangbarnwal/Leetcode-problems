class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq={}
        left=0
        maxcount=0
        maxlen=0
        for right in range(len(s)):
            if s[right] in freq.keys():
                freq[s[right]]+=1
            else:
                freq[s[right]]=1
            maxcount=max(maxcount,freq[s[right]])
            while (right-left+1)-maxcount>k:
                freq[s[left]]-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen
        