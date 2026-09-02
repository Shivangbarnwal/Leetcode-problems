class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        suma=0
        nums=list(nums)
        for i in nums:
            w=i%10
            d=str(i//10)
            x=int(d[:w])
            y=int(d[w:])
            suma=(suma+pow(x,y,10**9+7))%(10**9+7)
        return suma%(10**9+7)