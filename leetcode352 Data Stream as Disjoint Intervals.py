from collections import defaultdict
from typing import List

class SummaryRanges:
    def __init__(self):
        self.numToGroup = {}
        self.groupToNums = defaultdict(set)
        self.currGroup = 0

    def addNum(self, value: int) -> None:
        if value in self.numToGroup:
            return

        if value - 1 not in self.numToGroup and value + 1 not in self.numToGroup:
            self.numToGroup[value] = self.currGroup
            self.groupToNums[self.currGroup].add(value)
            self.currGroup += 1
        elif value - 1 in self.numToGroup and value + 1 in self.numToGroup:
            groupNumber1, groupNumber2 = self.numToGroup[value - 1], self.numToGroup[value + 1]
            self.numToGroup[value] = groupNumber1
            self.groupToNums[groupNumber1].add(value)
            self.mergeGroups(groupNumber1, groupNumber2)
        elif value - 1 in self.numToGroup:
            group = self.numToGroup[value - 1]
            self.numToGroup[value] = group
            self.groupToNums[group].add(value)
        else:
            group = self.numToGroup[value + 1]
            self.numToGroup[value] = group
            self.groupToNums[group].add(value)

    def mergeGroups(self, groupNumber1: int, groupNumber2: int):
        if groupNumber1 == groupNumber2:
            return

        # make sure group1 is always the bigger one
        if len(self.groupToNums[groupNumber1]) < len(self.groupToNums[groupNumber2]):
            groupNumber1, groupNumber2 = groupNumber2, groupNumber1

        for num in self.groupToNums[groupNumber2]:
            self.groupToNums[groupNumber1].add(num)
            self.numToGroup[num] = groupNumber1
        del self.groupToNums[groupNumber2]

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        for groupedNums in self.groupToNums.values():
            intervals.append([min(groupedNums), max(groupedNums)])

        return sorted(intervals)


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
