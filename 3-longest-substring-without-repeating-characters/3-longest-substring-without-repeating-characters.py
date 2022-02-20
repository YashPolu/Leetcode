class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s is None:
            return 0
        
        if len(s)<=1:
            return len(s)
        
        d = dict()
        start = longest = 0
        
        for i,c in enumerate(s):
            if c in d:
                start = max(start,d[c]+1)
            
            longest = max(longest,i-start+1)
            d[c] = i
        
        return longest
        
        
        
        