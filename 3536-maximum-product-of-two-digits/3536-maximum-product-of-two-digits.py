class Solution:
    def maxProduct(self, n: int) -> int:
        b=sorted(list(str(n)))
        return int(b[-1])*int(b[-2])