class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for idx,i in enumerate(nums):
            diff = target - i
            if diff in hm:
                return [hm[diff],idx]
            else:
                hm[i] = idx
        return [0,0]
        