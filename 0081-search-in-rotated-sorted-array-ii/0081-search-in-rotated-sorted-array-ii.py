class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[high] and nums[low]==nums[mid]:
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]:
                if nums[mid]>=target and nums[low]<=target:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target and nums[high]>=target:
                    low=mid+1
                else:
                    high=mid-1
        return False
        