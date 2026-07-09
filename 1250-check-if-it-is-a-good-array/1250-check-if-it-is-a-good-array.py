import math
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        
        g=nums[0]
        for i in nums:
            g=gcd(g,i)
        return g==1