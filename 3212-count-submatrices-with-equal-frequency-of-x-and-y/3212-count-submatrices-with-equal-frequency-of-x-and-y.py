class Solution(object):
    def numberOfSubmatrices(self, grid):
        suma=[]
        m=len(grid[0])
        n=len(grid)
        for i in range(len(grid)+1):
            test=[]
            for j in range(len(grid[0])+1):
                test.append([0,0])
            suma.append(test)
        c=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                suma[i][j][0]=suma[i][j-1][0]+suma[i-1][j][0]-suma[i-1][j-1][0]
                suma[i][j][1]=suma[i][j-1][1]+suma[i-1][j][1]-suma[i-1][j-1][1]
                if grid[i-1][j-1]=='X':
                    suma[i][j][0]+=1
                elif grid[i-1][j-1]=='Y':
                    suma[i][j][1]+=1
                
                if suma[i][j][0]==suma[i][j][1] and sum(suma[i][j])!=0:
                    c+=1
        return c
        
        
