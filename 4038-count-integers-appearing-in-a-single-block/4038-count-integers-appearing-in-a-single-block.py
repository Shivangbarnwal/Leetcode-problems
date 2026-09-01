from collections import defaultdict
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        prev=nums[0]
        mpp=defaultdict(int)
        mpp[prev]=1
        for i in range(1,len(nums)):
            k=nums[i]
            if prev!=k:
                mpp[k]+=1
                prev=k
        return list(mpp.values()).count(1)