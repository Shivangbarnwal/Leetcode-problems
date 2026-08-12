from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mpp=defaultdict(int)
        left=0
        count=0
        for right in range(n):
            mpp[nums[right]]+=1
            while mpp[nums[right]]>k:
                mpp[nums[left]]-=1
                left+=1
            count=max(count,right-left+1)
        return count