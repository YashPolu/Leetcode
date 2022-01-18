class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        
        l = len(f)
        count=0
        
        if f == [0]:
            return True
        
        for i in range(0,l-1):
            if i == 0:
                if f[i] == 0 and f[i+1] == 0:
                    count+=1
                    f[i] =1
                
            if f[i-1] == 0 and f[i+1] == 0 and f[i]!=1:
                f[i] = 1
                count+=1
            
            if i == l-2:
                if f[i] == 0 and f[i+1] == 0:
                    count+=1
        
        return count>=n
            
        
        