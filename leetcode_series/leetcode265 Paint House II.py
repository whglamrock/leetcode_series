class Solution(object):
    def minCostII(self, costs):

        # invalid null case
        if not costs or not costs[0]:
            return 0

        # when there is only one available color
        if len(costs[0]) == 1:
            if len(costs) > 1:
                return 2147483647   # or whatever other value
            else:
                return costs[0][0]

        n = len(costs)
        dp = [[0 for j in xrange(len(costs[0]))] for i in xrange(n)]
        dp[0] = costs[0]

        for i in xrange(1, n):
            # find the minvalue from previous dp[i]
            prevmin = min(dp[i - 1])

            # find all possible previous paint colors that can reach the previous minvalue
            prevminset = set()
            for j in xrange(len(costs[0])):
                if dp[i - 1][j] == prevmin:
                    prevminset.add(j)

            # find the second min value, in case that the current color
            #   is same as the color that reaches the previous minvalue
            prevsecondmin = 2147483647
            for j in xrange(len(costs[0])):
                if dp[i - 1][j] == prevmin:
                    continue
                if dp[i - 1][j] < prevsecondmin:
                    prevsecondmin = dp[i - 1][j]

            for j in xrange(len(costs[0])):
                if j not in prevminset:
                    dp[i][j] = prevmin + costs[i][j]
                else:
                    # means we have mutiple conbinations that reaches the previous minvalue
                    if len(prevminset) > 1:
                        dp[i][j] = prevmin + costs[i][j]
                    else:
                        dp[i][j] = prevsecondmin + costs[i][j]

        return min(dp[-1])