class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for each in encoded:
            arr.append(arr[-1]^each)
    
        return arr
        