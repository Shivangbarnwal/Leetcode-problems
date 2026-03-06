class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p=0
        c=0
        for i in s:
            if i=="1":
                if c==0:
                    p=1
                else:
                    return False
            if p==1 and i=="0":
                c=1
        return True