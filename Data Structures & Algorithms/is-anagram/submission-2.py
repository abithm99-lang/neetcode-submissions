class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick check: if lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False

        hmS = {}
        hmT = {}

        # Use range(len(s)) to get the index numbers
        for i in range(len(s)):
            char_s = s[i] # Use square brackets [] for indexing
            if char_s in hmS:
                hmS[char_s] += 1
            else:
                hmS[char_s] = 1

        for i in range(len(t)):
            char_t = t[i]
            if char_t in hmT:
                hmT[char_t] += 1
            else:
                hmT[char_t] = 1

        # Python can compare two dictionaries directly!
        return hmS == hmT
