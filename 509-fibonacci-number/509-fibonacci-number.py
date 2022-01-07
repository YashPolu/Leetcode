class Solution:
    def fib(self, n: int) -> int:
        dp = [0] *31
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
        