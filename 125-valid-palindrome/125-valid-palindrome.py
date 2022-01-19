class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        punc = string.punctuation
        new_s=re.sub(r'[^\w\s]', '', s).replace("_","").replace(" ","").lower()

        return new_s == new_s[::-1]
        