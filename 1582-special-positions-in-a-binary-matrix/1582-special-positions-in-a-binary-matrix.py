class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        check=[]
        for i in range(len(mat)):
            if sum(mat[i])==1:
                check.append(i)
        ans=0
        for i in check:
            suma=0
            for j in mat:
                suma+=j[i]
            if suma==1:
                ans+=1
        return ans
        