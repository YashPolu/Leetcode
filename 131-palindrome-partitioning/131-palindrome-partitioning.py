class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = list()
        part = list()
        
        def dfs(i):
            if i >= len(s):
                result.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.ispalin(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
            
        dfs(0)
        return result
    
    def ispalin(self,palin):
        return palin == palin[::-1]
                
        