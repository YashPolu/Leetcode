class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canfinsh(k):
            h_needed = 0
            
            for p in piles:
                h_needed += ceil(p/k)
            
            return h_needed <= h
            
            
        
        left = 1
        right = max(piles)
        
        while left < right:
            
            mid = left + (right - left)//2
            
            if canfinsh(mid):
                right = mid
            else:
                left = mid+1
        
        return right
        