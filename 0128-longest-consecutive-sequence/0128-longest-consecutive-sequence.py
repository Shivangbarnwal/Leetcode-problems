class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        numset=set(nums)
        longest=0
        
        for num in numset:
            if num-1 not in numset:
                count=1
                while num+count in numset:
                    count+=1
                longest=max(longest,count)
        return longest
        