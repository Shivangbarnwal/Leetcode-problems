class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        rep=0
        prev=""
        lst=[]
        for i in range(len(colors)):
            if colors[i]==prev:
                lst.append(neededTime[i])
            else:
                if len(lst)>1:
                    rep+=sum(lst)-max(lst)
                prev=colors[i]
                lst=[neededTime[i]]
        if len(lst)>1:
            rep+=sum(lst)-max(lst)
        return rep