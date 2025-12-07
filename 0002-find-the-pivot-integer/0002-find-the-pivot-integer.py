class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        suma=(n*(n+1))//2
        cur=0
        i=1
        while cur<suma:
            
            cur+=i
            suma-=i-1
            
            if cur==suma:
                return i
            i+=1
        return -1