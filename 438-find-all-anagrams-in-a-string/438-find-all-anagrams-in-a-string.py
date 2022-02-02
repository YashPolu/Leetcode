class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns,np = len(s),len(p)
        
        if ns< np:
            return []
        
        pc = Counter(p)
        sc = Counter()
        
        result = list()
        
        for i in range(ns):
            sc[s[i]] +=1
            
            if i >=np:
                if sc[s[i-np]] == 1:
                    del sc[s[i-np]]
                else:
                    sc[s[i-np]]-=1
                    
            if pc == sc:
                result.append(i-np+1)
                
        return result
            
        
        