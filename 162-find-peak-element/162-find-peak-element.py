class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        great = max(nums)
        
        if n == 1:
            return 0
        
        if n == 2:
            return nums.index(great)
        
        if nums == sorted(nums) or nums == sorted(nums,reverse=True):
            return nums.index(great) 
        
        
        if nums[0] == great:
            return 0
        
        if nums[-1] == great:
            return n-1
        
        for i in range(1,n-1):
            if (nums[i-1] < nums[i]) and (nums[i] > nums[i+1]):
                return i
        
            
            
            
            
            
        