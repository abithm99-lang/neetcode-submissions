class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hm = defaultdict(int)
        res = 0

        for right in range(len(s)):
            hm[s[right]] += 1

            while right - left +1 - max(hm.values()) > k:
                hm[s[left]]-=1
                left+=1
                    
            res = max(res, right - left + 1)

        return res
 
        