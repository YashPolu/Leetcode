class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        ns,np = len(s),len(p)
        
        if ns< np:
            return []
        
        pc = Counter(p)
        sc = Counter()
        
        
        for i in range(ns):
            sc[s[i]] +=1
            
            if i >=np:
                if sc[s[i-np]] == 1:
                    del sc[s[i-np]]
                else:
                    sc[s[i-np]]-=1
                    
            if pc == sc:
                return True
        
        return False
    
        
        