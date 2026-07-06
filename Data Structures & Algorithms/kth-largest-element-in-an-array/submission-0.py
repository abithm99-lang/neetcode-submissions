class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-num for num in nums]
        heapq.heapify(maxheap)
        while len(maxheap)>0:
            val= -heapq.heappop(maxheap)
            k-=1

            if k==0:
                return val