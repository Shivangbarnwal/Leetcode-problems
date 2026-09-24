class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for j in range(len(nums)):
            if j==sum([int(i) for i in list(str(nums[j]))]):
                return j
        return -1