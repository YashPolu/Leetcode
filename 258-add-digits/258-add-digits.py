class Solution:
    def sumed(self,n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r
    
    def addDigits(self, num: int) -> int:
        
        if num<=9:
            return num
        
        r = self.sumed(num)
        while r>9:
            r = self.sumed(r)
        
        return r
            
            
        