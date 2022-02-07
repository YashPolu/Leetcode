class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        d = int(num ** (0.5))
        
        return d**2 == num
        