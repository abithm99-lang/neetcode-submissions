class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=0:
            return 0
        maxCount = 0
        left = 0
        hs = set()
        for right in range(len(s)):
            while s[right] in hs:
                hs.remove(s[left])
                left+=1

            hs.add(s[right])
            maxCount = max(maxCount,right-left+1)

        return maxCount     


        