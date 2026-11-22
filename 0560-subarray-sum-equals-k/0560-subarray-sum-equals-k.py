from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum=0
        mpp=defaultdict(int)
        mpp[0]=1
        cnt=0
        for i in range(len(nums)):
            presum+=nums[i]
            cnt+=mpp[presum-k]
            mpp[presum]+=1
        return cnt