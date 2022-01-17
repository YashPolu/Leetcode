class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        d = defaultdict(list)
        words = s.split(" ")
        
        if len(p) != len(words):
            return False
        
        if len(set(p)) != len(set(words)):
            return False
        
        for a,b in zip(p,words):
            d[a].append(b)
            
        for key in d.keys():
            if len(set(d[key])) != 1:
                return False
        return True
        