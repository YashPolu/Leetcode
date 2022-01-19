class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        temp = x
        rev = 0
        
        while temp:
            div,carry = divmod(temp,10)
            rev = rev*10 + carry
            temp = div
        
        
        return rev == x
        