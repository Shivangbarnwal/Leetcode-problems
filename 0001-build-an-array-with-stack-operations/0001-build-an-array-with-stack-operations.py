class Solution(object):
    def buildArray(self, target, n):
        ans=[]
        ans.extend(["Push"]+["Push","Pop"]*(target[0]-1))
        for i in range(len(target)-1):
            ans.extend(["Push","Pop"]*(target[i+1]-target[i]-1))
            ans.append("Push")
        return ans



        