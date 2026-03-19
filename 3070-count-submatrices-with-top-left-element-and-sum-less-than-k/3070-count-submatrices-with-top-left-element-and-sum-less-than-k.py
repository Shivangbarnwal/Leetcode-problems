class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        suma=[]
        m=len(grid[0])
        n=len(grid)
        for i in range(len(grid)+1):
            suma.append([0]*(len(grid[0])+1))
        c=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                suma[i][j]=suma[i][j-1]+suma[i-1][j]-suma[i-1][j-1]
                suma[i][j]+=grid[i-1][j-1]
                
                if suma[i][j]<=k:
                    c+=1
        return c
        