class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        minodd=float('inf')
        mineven=float('inf')
        o=0
        e=0
        for i in nums:
            if i%2==0:
                mineven=min(mineven,i)
                e+=1
            else:
                minodd=min(minodd,i)
                o+=1
        if o==0 or e==0:
            return True
        if mineven>minodd:
            return True
        return False