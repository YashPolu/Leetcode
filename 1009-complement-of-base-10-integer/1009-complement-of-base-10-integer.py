class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n ==0:
            return 1
        
        flip, bit = n, 1
        while flip:
            n = n ^ bit
            bit = bit << 1
            flip = flip >> 1
            
        return n
            
        