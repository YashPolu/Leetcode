class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @lru_cache(maxsize=None)
        def dp(remain):
            if remain == 0:
                return False
            
            num = int(remain**0.5)
            
            for i in range(1,num+1):
                if not dp(remain-i*i):
                    return True
            
            return False
        
        return dp(n)
        