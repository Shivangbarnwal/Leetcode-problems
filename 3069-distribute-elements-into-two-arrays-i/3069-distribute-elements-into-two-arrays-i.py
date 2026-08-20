class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums1,nums2=[nums[0]],[nums[1]]
        i=0
        j=0
        for k in nums[2:]:
            if nums1[i]>nums2[j]:
                nums1.append(k)
                i+=1
            else:
                nums2.append(k)
                j+=1
        nums1.extend(nums2)
        return nums1