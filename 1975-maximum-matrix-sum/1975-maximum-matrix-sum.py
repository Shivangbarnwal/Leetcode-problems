class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        mini=float("inf")
        neg=0
        suma=0
        for i in matrix:
            for j in i:
                if j>0:
                    suma+=j
                else:
                    suma+=abs(j)
                    neg+=1
                mini=min(mini,abs(j))
        if neg%2==0:
            return suma
        else:
            return suma-(2*mini)
        