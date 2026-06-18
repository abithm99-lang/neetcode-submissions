class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)
        minK = right
        while left<=right:
            hrs = 0
            k = (left + right) //2
            for idx,pile in enumerate(piles):
                hrs += math.ceil(pile / k)
            
            if hrs>h:
                left = k+1             
            elif hrs<=h:
                minK = min(minK,k)
                right = k-1
                
        return minK



        