class Solution(object):
    def peakIndexInMountainArray(self, arr):
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            if (arr[mid+1]<arr[mid]) and (arr[mid-1]<arr[mid]):
                return mid
            elif arr[mid]<arr[mid+1]:
                left=mid+1
            else:
                right=mid-1

        