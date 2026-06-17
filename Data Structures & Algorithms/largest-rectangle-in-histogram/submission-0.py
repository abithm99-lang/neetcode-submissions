class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,ht in enumerate(heights):
            start = i
            while stack and stack[-1][1]>=ht:
                idx,val = stack.pop()
                maxArea = max((i-idx)*val,maxArea)
                start=idx
            stack.append([start,ht])

        while stack:
            idx,ht = stack.pop()
            lenght = len(heights)
            maxArea = max((lenght-idx)*ht,maxArea)
            
        return maxArea
