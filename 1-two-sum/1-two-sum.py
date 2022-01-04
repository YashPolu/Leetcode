class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_map = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in dict_map:
                return [i, dict_map[complement]]
            
            dict_map[nums[i]] = i
        
        
        
        
        