class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        ref = [collections.Counter(bin(num)[2:])['1'] for num in arr]      
        #print(ref)
        result = [x for y, x in sorted(zip(ref, arr))]
        
        return result