class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        k=[]
        l=sorted(nums)
        for i in range(len(nums)):
            if l[i]==target:
                k.append(i)
            elif l[i]>target:
                break
        return k