class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = dict()
        
        for a in nums1:
            for b in nums2:
                d[a+b] = d.get(a+b,0)+1
        
        count = 0

        for c in nums3:
            for e in nums4:
                r= -(c+e)
                a = d.get(r,0)
                count+=a
        
        return count
        