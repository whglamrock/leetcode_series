from collections import defaultdict
from time import time
from typing import List

class SnapshotArray:

    def __init__(self, length: int):
        self.indexToTimeToVal = defaultdict(dict)
        self.indexToTimeStamps = defaultdict(list)
        self.currentSnapId = 0
        self.snapIdToTimestamp = {}

    def set(self, index: int, val: int) -> None:
        timestamp = time()
        self.indexToTimeToVal[index][timestamp] = val
        self.indexToTimeStamps[index].append(timestamp)

    def snap(self) -> int:
        timestamp = time()
        self.snapIdToTimestamp[self.currentSnapId] = timestamp
        self.currentSnapId += 1
        return self.currentSnapId - 1

    def get(self, index: int, snap_id: int) -> int:
        timeStampOfSnap = self.snapIdToTimestamp[snap_id]
        earlierTimestamp = self.findLatestTimeEarlierThan(self.indexToTimeStamps[index], timeStampOfSnap)
        if earlierTimestamp != -1:
            return self.indexToTimeToVal[index][earlierTimestamp]
        # each element is initialized as 0
        return 0

    def findLatestTimeEarlierThan(self, timestamps: List[float], target: float) -> float:
        l, r = 0, len(timestamps) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if timestamps[m] <= target:
                    return timestamps[m]
                else:
                    return -1
            if timestamps[m] == target:
                return timestamps[m]
            elif timestamps[m] < target:
                l = m
            else:
                r = m - 1

        return -1


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
