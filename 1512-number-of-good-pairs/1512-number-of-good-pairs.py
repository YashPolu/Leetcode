class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        
        l = len(nums)
        
        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i] == nums[j] and i < j:
                    pairs+=1
        
        return pairs
                    
        