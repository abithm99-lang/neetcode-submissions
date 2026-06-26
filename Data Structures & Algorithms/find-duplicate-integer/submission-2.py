class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0,0

        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]] 
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

    # def findDuplicate(self, nums: List[int]) -> int:
    #     for i in range(len(nums)):
    #         val = abs(nums[i])
    #         target_idx = val-1
    #         if nums[target_idx]<0:
    #             return val
    #         nums[abs(nums[i])-1] *= -1
        
    #     return -1