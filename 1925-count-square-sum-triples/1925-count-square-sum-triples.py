from math import sqrt
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                c=int(sqrt(i**2+j**2+1))
                if c<=n and c**2==i**2+j**2:
                    ans+=1
        return ans
        
        