class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        dp = [0] * 1000
        
        trips.sort(key = lambda x: x[1])
        
        starts = [i[1] for i in trips]
        
        ends = [i[2] for i in trips]
        
        for i in range(len(trips)):
            for j in range(starts[i],ends[i]):
                dp[j] += trips[i][0]
                
        if max(dp) > capacity:
            return False
        else:
            return True
        
        
        
        
        