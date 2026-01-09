class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        hashmap={}
        for i in range(n):
            if nums[i] in hashmap.keys():
                return i,hashmap[nums[i]]
            hashmap[target-nums[i]]=i
        