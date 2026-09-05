class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi=[]
        cur=nums[-1]
        for i in nums[::-1]:
            cur=min(cur,i)
            maxi.append(cur)
        maxi=maxi[::-1]
        mini=0
        for i in range(len(nums)):
            mini=max(mini,nums[i])
            if (mini-maxi[i])<=k:
                return i
        return -1