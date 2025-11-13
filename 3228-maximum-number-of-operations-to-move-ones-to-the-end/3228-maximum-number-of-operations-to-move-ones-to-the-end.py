class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        cl=[]
        cr=0
        check=0
        for i in s:
            if i=="1":
                check=1
                cr+=1
            elif check==1:
                check=0
                cl.append(cr)
                cr=0
        op=0
        s=0
        for j in cl:
            s+=j
            op+=s
        return op
        