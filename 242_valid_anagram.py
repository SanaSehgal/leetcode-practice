class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        
        # Count characters in s
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        # Decrement counts for characters in t
        for j in t:
            if j not in d:
                return False
            d[j] -= 1
            if d[j] < 0:
                return False
        
        return True