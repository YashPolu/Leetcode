class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        length, b, f = 0, 0, {}
        for i, v in enumerate(nums):
            b += 1 if v else -1
            cur = i + 1 if not b else i - f.setdefault(b, i)
            length = max(length, cur)
        return length
        