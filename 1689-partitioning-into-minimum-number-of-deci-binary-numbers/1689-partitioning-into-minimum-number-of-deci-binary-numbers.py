class Solution:
    def minPartitions(self, n: str) -> int:
        ch = 0
        
        for num in n:
            ch = max(ch,int(num))
        
        return ch
        
        