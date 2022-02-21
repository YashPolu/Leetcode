class Solution:
    def get_key(self,my_dict,val):
        for key, value in my_dict.items():
            if val == value:
                return key
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        # ele = 
        
        return self.get_key(count,max(count.values()))
        
        
        