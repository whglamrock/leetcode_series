
# Basic idea: sort. P.S.: timepoints doesn't necessarily have to be in the same day

class Solution(object):
    def findMinDifference(self, timePoints):

        def standardize(hour, minute):
            return hour * 60 + minute

        pq = []
        for time in timePoints:
            hour, minute = time.split(':')
            hour, minute = int(hour), int(minute)
            standardtime = standardize(hour, minute)
            pq.append(standardtime)

        pq.sort()
        ans = pq[1] - pq[0]
        for i in xrange(1, len(pq)):
            ans = min(ans, pq[i] - pq[i - 1])
        ans = min(ans, pq[0] + 1440 - pq[-1])

        return ans