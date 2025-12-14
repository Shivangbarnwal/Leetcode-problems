class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        if corridor.count("S")%2!=0 or corridor.count("S")==0:
            return 0
        m=1
        c=0
        p=0
        for i in corridor:
            if c==2:
                if i=="P":
                    p+=1
                else:
                    m*=(p+1)
                    c=1
                    p=0
            elif i=="S":
                c+=1
        return m%(10**9+7)
            
            
        