class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        maxheap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                idx = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][idx]
                maxheap.append([count, tweetId, followeeId, idx-1])
        heapq.heapify(maxheap)

        while maxheap and len(res)<10:
            count, tweetId, followeeId, idx = heapq.heappop(maxheap)
            res.append(tweetId)
            if idx>=0:
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(maxheap,[count, tweetId, followeeId, idx-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
