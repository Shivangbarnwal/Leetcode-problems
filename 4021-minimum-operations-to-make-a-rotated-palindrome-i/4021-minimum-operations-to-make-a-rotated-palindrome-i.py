class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        c=float('inf')
        for i in range(n):
            temp=i
            for j in range(n//2):
                lol=abs(ord(s[j])-ord(s[-j-1]))
                temp+=min(lol,26-lol)
            c=min(c,temp)
            s=s[1:]+s[0]
        return c