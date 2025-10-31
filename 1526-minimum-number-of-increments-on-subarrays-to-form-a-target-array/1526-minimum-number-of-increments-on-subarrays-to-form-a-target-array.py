class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        count=0
        prev=0
        for i in target:
            if i>prev:
                count+=i-prev
            prev=i
        return count