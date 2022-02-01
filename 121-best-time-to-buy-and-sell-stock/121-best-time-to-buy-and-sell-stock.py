class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [0] *(l)
        lowest = prices[0]
        
        for p in range(1,l):
            lowest = min(lowest,prices[p])
            dp[p] = max(dp[p-1],prices[p]-lowest)
        
        return dp[-1]
        