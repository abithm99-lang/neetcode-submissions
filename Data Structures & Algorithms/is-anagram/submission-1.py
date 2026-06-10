class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        hmS, hmT = {}, {}
        
        # Loop directly through characters
        for char in s:
            hmS[char] = hmS.get(char, 0) + 1
            
        for char in t:
            hmT[char] = hmT.get(char, 0) + 1
            
        return hmS == hmT
