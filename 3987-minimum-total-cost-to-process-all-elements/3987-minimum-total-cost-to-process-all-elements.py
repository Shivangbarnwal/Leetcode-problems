class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        n= ((sum(nums)+k-1)//k)-1
        return ((n*(n+1))//2)%(10**9+7)