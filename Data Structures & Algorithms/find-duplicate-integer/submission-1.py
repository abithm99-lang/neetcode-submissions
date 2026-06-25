class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = abs(nums[i])
            target_idx = val-1
            if nums[target_idx]<0:
                return val
            nums[abs(nums[i])-1] *= -1
        
        return -1