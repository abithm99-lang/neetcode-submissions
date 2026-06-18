class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = float("infinity")
        l,r = 0,len(nums)-1

        

        while l<=r:

            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break

            mid = (l+r)//2
            minVal = min(minVal,nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1  
            elif nums[r] > nums[mid]:
                r = mid-1

        return minVal
              