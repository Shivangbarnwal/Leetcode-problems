class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mpp={}
        for i in s:
            mpp[i]=mpp.get(i,0)+1
        for j in range(len(s)):
            if mpp[s[j]]==1:
                return j
        return -1
        