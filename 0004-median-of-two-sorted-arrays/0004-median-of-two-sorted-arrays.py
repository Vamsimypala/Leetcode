class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        b=len(nums1)//2
        if len(nums1)%2 ==0:
            return (nums1[b] + nums1[b-1])/2
        else:
            return (nums1[b])
        