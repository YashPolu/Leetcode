class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane Algorithm
        
        current = max_subarray = nums[0]
        
        for num in nums[1:]:
            current = max(num,current+num)
            max_subarray = max(max_subarray,current)
        
        return max_subarray
        
        