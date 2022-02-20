class Solution:
    def removeCoveredIntervals(self, it: List[List[int]]) -> int:
        
        it.sort(key=lambda x: (x[0],-x[1]))
        result= l = len(it)
        start , end = it[0]

        for i in range(1,l):
            if start <= it[i][0] and it[i][1] <= end:
                result-=1
            else:
                start,end = it[i]
        
        return result
            
            
        
        
        