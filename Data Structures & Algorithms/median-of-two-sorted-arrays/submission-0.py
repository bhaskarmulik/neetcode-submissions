class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        p = sorted(nums1 + nums2)
        l = len(p)
        print(p)
        if l % 2 == 0:
            return (p[int(l/2)] + p[int((l/2)-1)])/2
        else:
            return p[l//2]