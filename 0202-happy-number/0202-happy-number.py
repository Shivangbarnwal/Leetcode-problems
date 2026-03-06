class Solution(object):
    def isHappy(self, n):
        s=set()
        while n!=1 and n not in s:
            s.add(n)
            total=0
            for i in str(n):
                total+=int(i)**2
            n=total
        return n==1
         