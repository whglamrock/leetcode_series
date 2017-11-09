
class Solution(object):
    def maxVacationDays(self, flights, days):

        ninf = -2147483648
        n, k = len(flights), len(days[0])
        # the best[i] means currently the max vacation we can have in city i;
        # initialize best[i] as negative infinite (not 0) because it could be no flights from/to city i
        best = [ninf] * n
        best[0] = 0  # we are always at city 0 at first

        for t in xrange(k):
            # at day t, update the best
            curr = [ninf] * n
            for i in xrange(n):
                for j in xrange(n):
                    if flights[i][j] or i == j:
                        # fly from city i to city j, so we need to look at the departure city's
                        #   best[i] on day t - 1 and search the max vacation days
                        #   of city j when there is available flight from i to j
                        curr[j] = max(curr[j], best[i] + days[j][t])
            best = curr

        return max(best)



flights = [[0,0,0],[0,0,0],[0,0,0]]
days = [[1,1,1],[7,7,7],[7,7,7]]
Sol = Solution()
print Sol.maxVacationDays(flights, days)
