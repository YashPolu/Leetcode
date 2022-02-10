class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = Counter()
        count[0] =1 
        
        sums = 0
        ans = 0
        
        for num in nums:
            sums+=num
            ans+=count[sums-k]
            count[sums]+=1
        
        return ans
        