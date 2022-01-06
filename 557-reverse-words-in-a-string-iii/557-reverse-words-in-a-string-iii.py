class Solution:
    def reverseWords(self, s: str) -> str:

        revwords = list()
        for i in s.split(" "):
            revwords.append(i[::-1]) 
        
        return " ".join(revwords)
        