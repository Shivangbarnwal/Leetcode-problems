class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        suma=0
        for i in t:
            suma+=ord(i)
        for j in s:
            suma-=ord(j)
        return chr(suma)
