
import heapq
class Twitter(object):

    def __init__(self):

        self.time = 0
        self.tweets = {}
        self.followee = {}

    def postTweet(self, user, tweet):   # tweet is the tweetId.

        self.time += 1
        if user in self.tweets:
            self.tweets[user].append((-self.time, tweet))
        else:
            self.tweets[user] = [(-self.time, tweet)]

    def getNewsFeed(self, user):

        h, tweets = [], self.tweets
        if user in self.followee:
            people = self.followee[user] | {user}   # '|' is the union of two sets
        else:
            people = {user}
        for person in people:
            if person in tweets and tweets[person]:
                time, tweet = tweets[person][-1]
                h.append((time, tweet, person, len(tweets[person]) - 1))
        heapq.heapify(h)
        news = []
        for _ in range(10):
            if h:
                time, tweet, person, idx = heapq.heappop(h)
                news.append(tweet)
                if idx > 0:
                    new_time, new_tweet = tweets[person][idx - 1]
                    heapq.heappush(h, (new_time, new_tweet, person, idx - 1))
        return news

    def follow(self, follower, other):

        if follower in self.followee:
            self.followee[follower].add(other)
        else:
            self.followee[follower] = {other}

    def unfollow(self, follower, other):

        if follower in self.followee and other in self.followee[follower]:
            self.followee[follower].remove(other)