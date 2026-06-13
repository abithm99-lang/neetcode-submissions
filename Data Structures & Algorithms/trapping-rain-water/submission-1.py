class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        MaxL = 0
        MaxR = 0
        left,right = 0,len(height)-1

        while left<=right:
            if height[left] < height[right]:
                MaxL = max(MaxL, height[left])
                trapped += max(0, MaxL - height[left])
                left+=1
            else:
                MaxR = max(MaxR,height[right])
                trapped += max(0, MaxR - height[right])
                right-=1
                
        return trapped            
            