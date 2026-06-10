class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False   
        h_set = {}
        for i in range(len(s)):
            h_set[s[i]] = h_set.get(s[i], 0) + 1
            h_set[t[i]] = h_set.get(t[i], 0) - 1

        return all(v == 0 for v in h_set.values())

        # if len(s)!=len(t):
        #     return False

        # hmS = {}
        # hmT = {}

        # for key in range(len(s)):
        #     if s[key] in hmS:
        #         hmS[s[key]]+=1
        #     hmS[s[key]] = 1

        # for key in range(len(t)):
        #     if t[key] in hmT:
        #         hmT[t[key]]+=1
        #     hmT[t[key]] = 1

        # return hmS == hmT
        