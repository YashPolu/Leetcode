class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxr = 0
        for s in sentences:
            a = s.split(" ")
            maxr = max(maxr,len(a))
        
        return maxr
        