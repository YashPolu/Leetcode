class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxr = 0
        r= 0 
        for i in gain:
            r= r+i
            maxr= max(maxr,r)
            
        return maxr
            