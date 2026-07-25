class Solution:
    def climbStairs(self, n: int) -> int:
        pre2,pre1=1,1
        for i in range(n-1):
            pre1,pre2=pre1+pre2,pre1
        return pre1