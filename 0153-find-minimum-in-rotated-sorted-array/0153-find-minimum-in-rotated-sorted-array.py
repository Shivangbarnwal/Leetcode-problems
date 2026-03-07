class Solution(object):
    def findMin(self, arr):
        start=0
        end=len(arr)-1
        while start<end:
            mid=(start+end)//2

            if arr[mid]<arr[end]:
                end=mid
            else:
                start=mid+1
        return arr[start]