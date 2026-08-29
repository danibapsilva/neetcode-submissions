class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # {userId: [timestamp, tweetID]}
        self.following = defaultdict(set) # (user_id: set(following_ids))
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timeStamp, tweetId])
        self.timeStamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [] # (timestamp, tweetId)
        
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            for timestamp, tweetId in self.tweets[followeeId]:
                heapq.heappush(heap, (timestamp, tweetId))

        return [heapq.heappop(heap)[1] for _ in range(min(10, len(heap)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
