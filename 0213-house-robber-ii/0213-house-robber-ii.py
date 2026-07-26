class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        pre1,pre2=0,0
        for i in nums[1:]:
            pre1,pre2=max(pre1,pre2+i),pre1
        m=pre1
        pre1,pre2=0,0
        for j in range(len(nums)-1):
            pre1,pre2=max(pre1,pre2+nums[j]),pre1
        m=max(m,pre1)
        return m