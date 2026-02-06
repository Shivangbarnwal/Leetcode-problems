class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        max_len = 0
        left = 0
    
        for right in range(n):
            # Move the left pointer to maintain the condition
            while nums[right] > nums[left] * k:
                left += 1
            max_len = max(max_len, right - left + 1)
        
        return n - max_len