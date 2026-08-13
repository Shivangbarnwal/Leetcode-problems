class Solution:
    def longestSubarray(self, arr: List[int]) -> int:
        idx=[]
        n=len(arr)
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                idx.append(i)
        maxi=1
        if idx==[]:
            return n
        for k in range(len(idx)):
            i = idx[k]
            larr,rarr=0,0
            if k>0:
                larr=i-idx[k-1]
            else:
                larr=i+1
            if k<(len(idx)-1):
                rarr=idx[k+1]-i
            else:
                rarr=n-i-1
            can_connect = False

            if i > 0 and arr[i - 1] <= arr[i + 1]:
                can_connect = True

            if i + 2 < n and arr[i] <= arr[i + 2]:
                can_connect = True

            if can_connect:
                maxi = max(maxi, larr + rarr)
            else:
                maxi = max(maxi, larr + 1, rarr + 1)

        return (maxi)