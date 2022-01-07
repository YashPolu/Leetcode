class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        count = collections.Counter(nums)
        
        for i in count.keys():
            if count[i] > 1:
                return True
        return False
        