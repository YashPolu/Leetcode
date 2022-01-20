class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def inlist(lst,num):
            if num in lst:
                return True
            else:
                return False
            
        # if len(matrix) == 1:
        #     return True if target in matrix else False
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m-1
        
        while left <= right:
            mid = left + (right - left) //2

            if target<matrix[mid][0]:
                right = mid -1
            
            elif target>matrix[mid][-1]:
                left = mid+1
            
            else:
                break
            
        
        return inlist(matrix[mid],target)
                
                
        