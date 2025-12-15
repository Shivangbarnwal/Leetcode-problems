class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def factorial(n):
            c=0
            while n>0:
                c+=n
                n-=1
            return c
        c=0
        n=len(prices)
        temp=1
        prev=prices[0]
        for i in range(1,n):
            if prices[i]==prev-1:
                temp+=1
                prev=prices[i]
            else:
                c+=factorial(temp)
                temp=1
                prev=prices[i]
        c+=factorial(temp)
        return c
