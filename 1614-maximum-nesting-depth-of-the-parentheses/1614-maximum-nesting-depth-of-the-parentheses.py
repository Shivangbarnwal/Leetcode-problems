class Solution:
    def maxDepth(self, k: str) -> int:
        s=0
        m=0
        for i in k:
            if i=="(":
                s+=1
                m=max(m,s)
            elif i==")":
                s-=1
        return m