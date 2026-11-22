class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums==[]:
            return 0
        arr=set(nums)
        longest=0
        for i in arr:
            if i-1 not in arr:
                count=1
                while i+count in arr:
                    count+=1
                longest=max(longest,count)
        return longest