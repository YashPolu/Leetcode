class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r'[A-Z]*|[A-Z][a-z]+|[a-z]*',word)
        