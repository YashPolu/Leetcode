class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        x = len(grid)
        y = len(grid[0])
        
        if not grid or x==0 or y==0:
            return None
        
        perimeter = 0
        
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    perimeter +=4
                    
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                        
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        
        return perimeter
                        
                    
                    
        