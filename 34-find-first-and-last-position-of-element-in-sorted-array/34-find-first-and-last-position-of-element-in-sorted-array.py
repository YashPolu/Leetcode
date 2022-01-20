class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        locations = list()
        
        for i in range(n):
            if nums[i] == target:
                locations.append(i)
        
        if len(locations) > 0:
            return [locations[0],locations[-1]]
        else:
            return [-1,-1]
                