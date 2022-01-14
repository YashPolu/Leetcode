class Solution:
    def myAtoi(self, s: str) -> int:
        
        ans, is_ws, is_neg = 0, True, False
        for char in s:
            if is_ws:
                if char == " ":
                    continue
                    
                # change the flag of whitespace to False if char is other than " "
                
                elif char == "+" or char == "-":                    
                    is_ws = False
                    is_neg = True if char == "-" else False
                    
                elif char.isdigit():
                    is_ws = False
                    ans = ans * 10 + ord(char) - ord('0')
                    
                else:
                    return 0
                
            else:
                
                if char.isdigit():
                    ans = ans * 10 + ord(char) - ord('0')
                else:
                    break
        
        return max(-2**31, -1 * ans) if is_neg else min(2**31 - 1, ans)
        