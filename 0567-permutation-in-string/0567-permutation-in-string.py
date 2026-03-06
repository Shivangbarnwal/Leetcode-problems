from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        req=defaultdict(int)
        for i in s1:
            req[i]+=1
        left=0
        win=defaultdict(int)
        if len(s1)>len(s2):
            return False
        for right in range(len(s2)):

            win[s2[right]]+=1
            if (right-left+1)>len(s1):
                win[s2[left]]-=1
                if win[s2[left]]==0:
                    del win[s2[left]]
                left+=1
            if win==req:
                return True
        return False


        