
# using orderedSet to maintain the order of popped out numbers can achieve O(logN) for pop operation
# but it will also increase the time for addBack to O(logN). So below solution is OK in real interview,
# and we just need to briefly explain the tradeoff.
class SmallestInfiniteSet:
    def __init__(self):
        self.deleted = set()
        self.currMin = 1

    def popSmallest(self) -> int:
        tmp = self.currMin
        self.deleted.add(tmp)

        self.currMin += 1
        while self.currMin in self.deleted:
            self.currMin += 1

        return tmp

    def addBack(self, num: int) -> None:
        self.deleted.discard(num)
        self.currMin = min(self.currMin, num)
