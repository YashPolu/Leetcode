class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2: 
            return False

        target = [0 for _ in range(26)]
        window = [0 for _ in range(26)]

        for i in range(n1):
            target[ord(s1[i]) - 97] += 1
            window[ord(s2[i]) - 97] += 1

        if(target == window):
            return True

        for i in range(n1, n2):
            window[ord(s2[i - n1]) - 97] -= 1
            window[ord(s2[i]) - 97] += 1

            if target == window:
                return True

        return False
                