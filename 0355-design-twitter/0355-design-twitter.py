class Twitter:

    def __init__(self):
        self.following=defaultdict(set)
        self.tweets=defaultdict(list)
        self.prio=0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.tweets:
            self.tweets[userId]=[]
        self.tweets[userId].append((self.prio,tweetId))
        self.prio-=1
    def getNewsFeed(self, userId: int) -> List[int]:
        tweetList=[]
        
        for followee in self.following[userId]:
            tweetList=tweetList+self.tweets[followee]
        tweetList=tweetList+self.tweets[userId]
        heapify(tweetList)
        print(tweetList)
        result=[]
        while tweetList:
            if len(result)==10:
                break
            result.append(heappop(tweetList)[1])
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)