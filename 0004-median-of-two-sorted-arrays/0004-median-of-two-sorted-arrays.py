class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        k=len(nums)
        if(k%2==0):
            median=(nums[k//2]+nums[(k//2)-1])/2.0
        else:
            median=nums[k//2]
        return median

        