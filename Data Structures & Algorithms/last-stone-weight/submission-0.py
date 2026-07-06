class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            first,second = heapq.heappop(maxheap),heapq.heappop(maxheap)
            diff = first - second
            if diff<0:
                heapq.heappush(maxheap,diff)
        return -maxheap[0] if len(maxheap)>0 else 0