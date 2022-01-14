class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        return set(nums1).intersection(set(nums2))
        
        
        
        
#         result = list()
        
#         counter1= collections.Counter(nums1)
#         counter2= collections.Counter(nums2)
        
#         for key in counter1.keys():
#             if key in counter2.keys():
#                 result.append(key)
        
#         return result
        
        