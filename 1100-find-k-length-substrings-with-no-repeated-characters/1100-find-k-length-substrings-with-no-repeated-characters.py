class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        l = len(s)
        
        if k > l:
            return 0
        
        count = 0 
        d = Counter()
        
#         if len(d.keys()) == k:
#             count+=1
        
        for i in range(l):
            d[s[i]]+=1
            
            if i >= k:
                if d[s[i-k]] == 1:
                    del d[s[i-k]]
                else:
                    d[s[i-k]]-=1
        
            if len(d.keys()) == k:
                count+=1
            
        
        return count
                
        
        
        