class Solution:
    def removeVowels(self, s: str) -> str:
        result = re.sub(r'[aeiou]', '', s)
        return result
        