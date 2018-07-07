
class Solution(object):
    def minCostClimbingStairs(self, cost):

        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        n = len(cost)
        cheapest = [0 for i in xrange(n + 1)]

        for i in xrange(2, n + 1):
            cheapest[i] = min(cheapest[i - 1] + cost[i - 1], cheapest[i - 2] + cost[i - 2])

        return cheapest[-1]



cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print Solution().minCostClimbingStairs(cost)

