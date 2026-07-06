class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            maxheap = [[-((x**2)+(y**2)),x,y] for x,y in points]
            heapq.heapify(maxheap)
            while len(maxheap)>k:
                heapq.heappop(maxheap)
            return [[x,y] for dist, x, y in maxheap]

        