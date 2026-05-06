class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        mat=[]
        
        n=len(boxGrid)
        m=len(boxGrid[0])

        for i in range(n):
            temp=["."]*(m)
            bot=0
            for j in range(m):
                k=boxGrid[i][-j-1]
                if k=="#":
                    temp[bot]=k
                    bot+=1
                elif k=="*":
                    temp[j]=k
                    bot=j+1
            mat.insert(0,temp[::-1])
        ans=[["." for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i]=mat[i][j]
        return ans

        


