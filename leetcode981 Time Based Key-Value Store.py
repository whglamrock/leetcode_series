from collections import defaultdict
from typing import List


class TimeMap:
    def __init__(self):
        self.keyToTimes = defaultdict(list)
        self.keyToTimeToValue = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToTimes[key].append(timestamp)
        self.keyToTimeToValue[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyToTimes:
            return ''

        # find the previous timestamp that's <= timestamp
        times = self.keyToTimes[key]
        maxTimestampEarlier = self.findMaxElementLessOrEqualThan(times, timestamp)
        if maxTimestampEarlier == -1:
            return ''

        return self.keyToTimeToValue[key][maxTimestampEarlier]

    def findMaxElementLessOrEqualThan(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if nums[m] <= target:
                    return nums[m]
                return -1

            if nums[m] <= target:
                l = m
            else:
                r = m - 1

        return -1
