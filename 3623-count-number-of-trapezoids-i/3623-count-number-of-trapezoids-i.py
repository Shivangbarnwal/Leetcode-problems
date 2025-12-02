class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x={}
        for i in points:
            if i[1] in x.keys():
                x[i[1]]+=1
            else:
                x[i[1]]=1
        newm=[]
        for j in x.values():
            ans=(j*(j-1))//2
            if ans>0:
                newm.append(ans)
        
        suma=0
        if len(newm)<2:
            return suma
        total_sum = sum(newm)
        square_sum = sum(c * c for c in newm)

        return (total_sum * total_sum - square_sum) // 2