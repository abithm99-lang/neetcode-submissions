class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = float("infinity")
        l,r = 0,len(nums)-1


        while l<=r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        return nums[m]

        

        # while l<=r:
        #     # when a number is sorted [4,5,6,7,0,1,2,3]
        #     #                      l is here-->|     | <-- r is here
        #     # at this case we need to save the min value and break
        #     if nums[l] < nums[r]:
        #         minVal = min(minVal, nums[l])
        #         break

        #     mid = (l+r)//2
        #     minVal = min(minVal,nums[mid])

        #     if nums[l] <= nums[mid]:
        #         l = mid + 1  
        #     elif nums[r] > nums[mid]:
        #         r = mid-1

        # return minVal
              