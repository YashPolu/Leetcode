class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        #running sum of products
        minprodsum = 0
        
        #iterate through each list together sorted in reverse directions:
        for (num1,num2) in zip(sorted(nums1),sorted(nums2,reverse = True)):
            minprodsum += (num1*num2)
        
        return(minprodsum)