class Solution:
    def removeVowels(self, s: str) -> str:
        result = re.sub(r'[AEIOU]', '', s, flags=re.IGNORECASE)
        return result
        