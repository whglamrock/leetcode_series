
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):

        if not timeSeries: return 0

        ans = 0
        # the start marks the start of current ongoing poisoning effect
        start = timeSeries[0]
        # the end marks the timing when poison loses effect if without availble further extension
        end = timeSeries[0] + duration

        for i in xrange(1, len(timeSeries)):
            if timeSeries[i] > end:
                ans += end - start
                start, end = timeSeries[i], timeSeries[i] + duration
            else:
                end = timeSeries[i] + duration
        ans += end - start

        return ans



Sol = Solution()
timeSeries = [1,4,5,6,7,12,14,18]
duration = 3
print Sol.findPoisonedDuration(timeSeries, duration)
