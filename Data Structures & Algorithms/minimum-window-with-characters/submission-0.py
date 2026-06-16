class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        res, resLen = [-1,-1] , float("infinity")
        org,hm = {}, {}

        for char in t:
            org[char]=org.get(char,0)+1
            
        have, need = 0, len(org)
        l=0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r],0)+1

            if s[r] in org and hm[s[r]] == org[s[r]]:
                have+=1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                hm[s[l]] = hm.get(s[l])-1
                if s[l]in org and hm[s[l]] < org[s[l]]:
                    have-=1
                l+=1
            
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
                
