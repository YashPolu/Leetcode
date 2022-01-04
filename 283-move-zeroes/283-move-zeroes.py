class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        if n == 1:
            return nums
        
        tortise = 0
        
        for hare in range(n):
            if nums[hare] != 0 and nums[tortise] == 0:
                nums[hare], nums[tortise] = nums[tortise],nums[hare]
            
            if nums[tortise] != 0:
                tortise+=1
        