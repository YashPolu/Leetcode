class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        # If len of s1 is greater than s2, then permutation is not possible
        if (n > m):
            return False
        
        # Create 2 arrays of size 26 to store frequency of letters
        x = [0] * 26
        y = [0] * 26
        
        # Counting Frequency of s1 and storing it in 'array y'
        for i in s1:
            y[(ord(i) - ord('a'))] += 1
        
        # Counting Frequency of first s1.length th letters and storing them in 'array x'
        for i in range(n):
            x[(ord(s2[i]) - ord('a'))] += 1
        
        # Checking whether the first 's1 length'th letters are permutation of s1
        if (x == y):
            return True
        
        # Else iterating a sliding window until we get permutation or array ends
        start = 0
        for i in range(n,m):
            x[(ord(s2[start]) - ord('a'))] -= 1
            x[(ord(s2[i]) - ord('a'))] += 1
            start += 1
            if (x == y):
                return True
        return False