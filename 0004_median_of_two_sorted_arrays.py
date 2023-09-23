class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1+nums2)
        size = len(merged)
        
        if size%2 != 0:
            ans = merged[(size+1)//2 - 1]
        else:
            ans = (merged[size//2 - 1] + merged[size//2])/2
        
        return ans
