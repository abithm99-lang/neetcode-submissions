class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0,len(heights)-1
        water = 0
        while left < right:
            waterStored = 0
            if heights[left]<heights[right]:
                contains = heights[left] * (right-left)
                water = max(contains,water)
                left+=1
            elif heights[left]>heights[right]:
                contains = heights[right] * (right-left)
                water = max(contains,water)
                right-=1
            else:
                contains = heights[right] * (right-left)
                water = max(contains,water)
                left+=1

        return water
        