class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        k=[i for i in str(n) if i!="0"]
        return int("".join(k))*sum(map(int,k))
        