class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s1,s2=0,0
        sq1,sq2=0,0
        for i in nums:
            s1+=i
            sq1+=i*i
        for j in range(1,len(nums)+1):
            s2+=j
            sq2+=j*j
        suma=int((sq2-sq1)/(s2-s1))
        diff=s2-s1
        return [int((suma-diff)/2),int((suma+diff)/2)]