class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        count = 0
        
        if arr[0]==max(arr) or arr[-1] == max(arr):
            return False
        
        for num in range(1,n-1):
            if arr[num-1] < arr[num] and arr[num] > arr[num+1]:
                count+=1
            if arr[num-1] >= arr[num] and arr[num] <= arr[num+1]:
                return False
        
        return count == 1
        
        