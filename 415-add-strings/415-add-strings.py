class Solution:
    def strtonum(self,num):
        result = 0
        for n in num:
            val = ord(n) - ord('0')
            result= result*10 +val
        
        return result
    
    def addStrings(self, num1: str, num2: str) -> str:
        output = self.strtonum(num1) + self.strtonum(num2)
        
        return str(output)
        
        