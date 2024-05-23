
class HitCounter:
    def __init__(self):
        self.prefixSum = []
        self.count = 0

    def hit(self, timestamp: int) -> None:
        self.count += 1
        if self.prefixSum and self.prefixSum[-1][0] == timestamp:
            self.prefixSum[-1][1] += 1
        else:
            self.prefixSum.append([timestamp, self.count])

    def getHits(self, timestamp: int) -> int:
        indexOf5MinEarlier = self.findIndexSmallerOrEqualThan(timestamp - 300)
        indexOfCurrent = self.findIndexSmallerOrEqualThan(timestamp)
        if indexOf5MinEarlier == -1:
            if indexOfCurrent != -1:
                return self.prefixSum[self.findIndexSmallerOrEqualThan(timestamp)][1]
            else:
                return 0
        else:
            return self.prefixSum[self.findIndexSmallerOrEqualThan(timestamp)][1] - \
                self.prefixSum[self.findIndexSmallerOrEqualThan(timestamp - 300)][1]

    # find the max index <= targetTime
    def findIndexSmallerOrEqualThan(self, targetTime: int) -> int:
        l, r = 0, len(self.prefixSum) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if self.prefixSum[m][0] <= targetTime:
                    return m
                return -1
            if self.prefixSum[m][0] <= targetTime:
                l = m
            else:
                r = m - 1

        return -1


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


'''
# a Naive O(n) time getHits solution
class HitCounter:
    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300
        # the hits in this index is more than 300 seconds old
        if self.times[i] != timestamp:
            self.hits[i] = 1
            self.times[i] = timestamp
        else:
            self.hits[i] += 1

    def getHits(self, timestamp: int) -> int:
        totalHits = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                totalHits += self.hits[i]

        return totalHits
'''