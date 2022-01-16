class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        n = len(seats)
        s = [i for i in range(n) if seats[i]]
        d = [s[i+1]-s[i] for i in range(len(s)-1)] if len(s) > 1 else [0]
        
        return max(max(d)//2, s[0], n-1-s[-1])
        