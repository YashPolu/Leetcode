class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        r = {}
        for i, k in enumerate(sorted(nums)):
            r.setdefault(k, i)
        return [r[k] for k in nums]
        