class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        result = list()
        
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        
        return result
        