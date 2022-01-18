class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        i,count = 0,0
        l = len(f)
        
        while i< l:
            if f[i] == 0 and (i == 0 or f[i-1] == 0) and (i== l-1 or f[i+1] == 0):
                f[i] = 1
                i+=1
                count+=1
            
            if count>=n:
                return True
            
            i+=1
        
        return False
                
            