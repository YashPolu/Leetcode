class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # print(max(max(trips)))
        
        dp = [0] * 1000
        
        trips.sort(key = lambda x: x[1])

        for i in trips:
            for j in range(i[1],i[2]):
                dp[j] += i[0]
                
        return max(dp) <= capacity
        
        
        
        
        