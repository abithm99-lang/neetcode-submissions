class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for key in nums:
            if key in hm:
                return True
            hm[key] = 1
        return False
        