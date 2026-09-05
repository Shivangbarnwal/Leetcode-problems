from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mpp=defaultdict(int)
        for i in range(min(k+1,len(nums))):
            mpp[nums[i]]+=1
        if max(mpp.values())>1:
            return True
        for j in range(k+1,len(nums)):
            mpp[nums[j-k-1]]-=1
            mpp[nums[j]]+=1
            if mpp[nums[j]]>1:
                return True
        return False