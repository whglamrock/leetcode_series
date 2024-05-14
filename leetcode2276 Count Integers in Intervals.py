from sortedcontainers import SortedList

class CountIntervals:
    def __init__(self):
        self.integerCount = 0
        self.intervals = SortedList()

    def add(self, left: int, right: int) -> None:
        i = self.intervals.bisect_left([left, right])
        while i < len(self.intervals) and self.intervals[i][0] <= right:
            # O(log(N)) for deleting an element by index
            l, r = self.intervals.pop(i)
            self.integerCount -= r - l + 1
            right = max(right, r)  # right is only actually updated in the last while loop
            # no need to do i++ here because we popped an element above

        if i > 0 and left <= self.intervals[i - 1][1]:
            l, r = self.intervals.pop(i - 1)
            self.integerCount -= r - l + 1
            left = l
            # it's possible the above while loop doesn't run and l < left < right < r
            right = max(right, r)

        self.integerCount += right - left + 1
        self.intervals.add([left, right])

    def count(self) -> int:
        return self.integerCount


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
