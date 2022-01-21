class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1+nums2)
        
        n = len(res)
        
        left = 0
        right = n-1
        
        mid = left + (right -left)//2
        
        if n%2 != 0:
            mid = left + (right -left)//2
            return float(res[mid])
        
        else:
            return (res[mid]+res[mid+1])/2

            
        
        