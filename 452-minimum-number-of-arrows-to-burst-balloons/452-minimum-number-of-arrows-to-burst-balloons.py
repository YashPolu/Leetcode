class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        arrows = 1
        
        if len(points) ==1 :
            return arrows
        
        points.sort(key= lambda x:x[1])
        
        first_end = points[0][1]
        
        for start,end in points:
            if first_end < start:
                arrows+=1
                first_end = end
        
        return arrows
        
        