class Solution(object):
    def findMin(self, arr):
        start=0
        end=len(arr)-1
        mini=float('inf')
        while start<=end:
            mid=(start+end)//2

            if arr[mid]<arr[end]:
                mini=min(mini,arr[mid])
                end=mid-1
            else:
                mini=min(mini,arr[start])
                start=mid+1
        return mini