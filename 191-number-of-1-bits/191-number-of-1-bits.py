class Solution:
    def hammingWeight(self, n: int) -> int:
        a = bin(n)[2:]
        count = collections.Counter(a)
        
        return count['1']