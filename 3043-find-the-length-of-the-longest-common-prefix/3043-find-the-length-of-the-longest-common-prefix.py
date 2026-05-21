class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        myset=set([])
        for i in arr1:
            s=str(i)
            su=""
            for j in s:
                su+=j
                myset.add((su))
        maxlen=0
        for i in arr2:
            s=str(i)
            su=""
            for j in s:
                su+=j
                if su in myset:
                    maxlen=max(maxlen,len(su))
        return maxlen
