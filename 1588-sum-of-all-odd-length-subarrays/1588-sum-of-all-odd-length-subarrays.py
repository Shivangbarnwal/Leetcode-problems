class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        suma=0
        for i in range(n):
            temp=0
            for j in range(i,n):
                temp+=arr[j]
                if (j-i+1)%2==1:
                    
                    suma+=temp
        return suma
        