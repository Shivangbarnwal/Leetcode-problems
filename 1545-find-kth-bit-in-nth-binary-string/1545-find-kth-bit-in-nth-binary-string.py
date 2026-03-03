class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        rev=0
        while n>1:
            temp=(2**n)-1
            if k==(temp+1)//2:
                return (str(abs(1-rev)))
            elif k>(temp+1)//2:
                rev=abs(1-rev)
                k=temp-k+1
            n-=1
        return (str(0+rev))
        