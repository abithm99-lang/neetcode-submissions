class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = [float("Infinity"),-1,-1]
        l = 0
        minVal = float("Infinity")
        t = 0
        for r in range(len(nums)):
            t+=nums[r]
            while t >= target:
                if r-l+1 < res[0]:
                    # minVal = min(minVal,t) 
                    res = [r-l+1,l,r]
                t-=nums[l]
                l+=1
        return res[0] if res[0]!=float("Infinity") else 0
            
