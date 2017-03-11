
# For a specific W, after choosing the biggest available benefit, the W will increase.
#   so no need to worry about better solutions.
# Also, we need to pop the chosen benefit from our choices pool, so we need PriorityQueue

from heapq import *

class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):

        if not Profits or not Capital:
            return 0

        n = len(Profits)
        benefits = sorted(zip(Profits, Capital), key = lambda x: x[1])
        pq = []

        j = 0
        for i in xrange(k):
            while j < n:
                if benefits[j][1] > W:
                    break
                heappush(pq, -benefits[j][0])
                j += 1
            if pq:
                biggestbenefit = -heappop(pq)
                W += biggestbenefit
            else:
                break

        return W



Sol = Solution()
print Sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1])
