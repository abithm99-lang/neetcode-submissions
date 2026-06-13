class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= set()
        nums.sort()

        for i,val in enumerate(nums):
            left,right = i+1,len(nums)-1
            while left < right:
                sum = val + nums[left] + nums[right]
                if sum == 0:
                    res.add((val, nums[left], nums[right]))
                    left+=1
                    right-=1
                elif sum > 0:
                    right-=1
                else:
                    left+=1

        return [list(lst) for lst in res]
