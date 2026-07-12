class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to={}
        sor=sorted(arr)
        rank=1
        for i in range(len(sor)):
            if i>0 and sor[i]>sor[i-1]:
                rank+=1
            num_to[sor[i]]=rank
        for i in range(len(arr)):
            arr[i]=num_to[arr[i]]
        return arr