class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = list()
        t_stack = list()
        
        for char in s:
            if char != '#':
                s_stack.append(char)
            elif len(s_stack) >0 and char == '#':
                s_stack.pop()
            else:
                continue
        
        for char in t:
            if char != '#':
                t_stack.append(char)
            elif len(t_stack) >0 and char == '#':
                t_stack.pop()
            else:
                continue
        
        print(s_stack,t_stack)
        
        return s_stack == t_stack
        
        