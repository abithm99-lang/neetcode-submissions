class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-t for t in count.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0
        while  maxheap or q:
            time+=1
            if maxheap:
                val = 1 + heapq.heappop(maxheap)  
                if val:
                    q.append([val,time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
                
        return time
        