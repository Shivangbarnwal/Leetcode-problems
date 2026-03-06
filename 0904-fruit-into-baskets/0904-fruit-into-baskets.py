class Solution(object):
    def totalFruit(self, fruits):
        mpp={}
        left=0
        maxlen=0
        for right in range(len(fruits)):
            if fruits[right] not in mpp.keys():

                mpp[fruits[right]]=1
            else:
                mpp[fruits[right]]+=1
            while len(mpp)>2:
                mpp[fruits[left]]-=1
                if mpp[fruits[left]]==0:
                    del mpp[fruits[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen