class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # stack approach
        max_len , stack = 0, list()
        
        for symbol in s:
            if symbol not in stack:
                stack.append(symbol)
                max_len = max(max_len,len(stack))
            else:
                stack.append(symbol)
                stack = stack[stack.index(symbol)+1:]
        
        return max_len
        
        