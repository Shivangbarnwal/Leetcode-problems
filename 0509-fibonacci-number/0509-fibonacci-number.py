class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def fib(n):
            if n<=0:
                return 0
            if n==1:
                return 1
            else:
                return fib(n-1)+fib(n-2)
        return fib(n)
        