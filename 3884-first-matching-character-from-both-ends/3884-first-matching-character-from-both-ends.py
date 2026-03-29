class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range((len(s)+1)//2):
            if s[i]==s[-i-1]:
                return i
        return -1