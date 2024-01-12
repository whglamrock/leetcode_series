
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


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
