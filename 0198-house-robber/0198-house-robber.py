class Solution:
    def rob(self, nums: List[int]) -> int:
        pre1=0
        pre2=0
        for i in nums:
            pre1,pre2=max(pre1,i+pre2),pre1
        return pre1