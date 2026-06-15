class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hm={}
        for char in s1:
            hm[char]=hm.get(char,0)+1

        for i in range(len(s1)):
            char = s2[i]
            if char in hm:
                hm[char] -= 1 

        if all(val == 0 for val in hm.values()):
            return True

        for i in range(len(s1),len(s2)):
            incoming = s2[i]
            outgoing = s2[i - len(s1)]
            if incoming in hm:
                hm[incoming] -= 1
            if outgoing in hm:
                hm[outgoing] += 1
            if all(val == 0 for val in hm.values()):
                return True
        
        return False
        