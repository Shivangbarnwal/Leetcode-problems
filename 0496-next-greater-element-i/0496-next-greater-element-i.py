class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n=len(nums2)
        stack=[]
        mpp={}
        for i in nums2:
            while stack and stack[-1]<i:
                mpp[stack.pop()]=i
            stack.append(i)
        while stack:
            mpp[stack.pop()]=-1
        return [mpp[i] for i in nums1]