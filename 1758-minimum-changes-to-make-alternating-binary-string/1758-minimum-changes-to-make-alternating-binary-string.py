class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        c=0
        for i in range(n):
            if s[i]!=str(i%2):
                c+=1
        c=min(c,n-c)
        return c
        