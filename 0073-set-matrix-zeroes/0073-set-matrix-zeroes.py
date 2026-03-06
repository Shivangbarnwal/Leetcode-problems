class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        r=[0]*m
        c=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    r[i]=1
                    c[j]=1
        for i in range(m):
            if r[i]==1:
                matrix[i]=[0]*n
        for i in range(n):
            if c[i]==1:
                for j in range(m):
                    matrix[j][i]=0
        return matrix
        
        
        
        