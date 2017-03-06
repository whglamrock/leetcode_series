class Solution(object):
    def candy(self, ratings):

        if len(ratings) <= 1:
            return 1

        candies = [1 for i in xrange(len(ratings))]
        # make sure from left to right fulfill requirements
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = max(candies[i], candies[i - 1] + 1)

        # make sure from right to left fulfill requirements
        for i in xrange(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)

        return sum(candies)