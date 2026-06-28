class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

################ TC of (n+n) ################
        if k > len(s):
            return 0

        l = r = 0
        hm = {}
        res = 0
        maxF = 0
        for r in range(len(s)):
            char = s[r]
            hm[char] = hm.get(char,0)+1
            maxF = max(maxF,hm[char])

            if (r-l+1) - maxF > k:
                hm[s[l]]-=1
                l+=1
            
            res = max(r-l+1,res)
        
        return res
        
################ TC of (n+n)* 26 ################
        left = 0
        hm = defaultdict(int)
        res = 0

        for right in range(len(s)):
            hm[s[right]] += 1

            while right - left +1 - max(hm.values()) > k: # check the (length - max count of the hm of most common element) which gives the other left over of how many needs to be changed
                hm[s[left]]-=1
                left+=1
                    
            res = max(res, right - left + 1)

        return res
 
        