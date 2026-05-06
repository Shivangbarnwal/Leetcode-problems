class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        
        n=len(boxGrid)
        m=len(boxGrid[0])
        ans=[["." for _ in range(n)] for _ in range(m)]
        for i in range(n):
            bot=m-1
            for j in range(m-1,-1,-1):
                
                if boxGrid[i][j]=="*":
                    ans[j][n-i-1]="*"
                    bot=j-1
                elif boxGrid[i][j]=="#":
                    ans[bot][n-1-i]="#"
                    bot-=1
           
        return ans

        


