class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res=0
        a2=sorted(arr2)
        for i in arr1:
            flag=True
            left=0
            right=len(a2)-1
            while left<=right:
                mid=(left+right)//2
                if abs(a2[mid]-i)<=d:
                    flag=False
                    break
                elif a2[mid]>i:
                    right=mid-1
                else:
                    left=mid+1
            if flag:
                res+=1
        return res