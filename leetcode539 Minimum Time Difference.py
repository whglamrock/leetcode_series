from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for time in timePoints:
            hour, minute = time.split(':')
            hour, minute = int(hour), int(minute)
            standardTime = self.standardizeTime(hour, minute)
            times.append(standardTime)

        times.sort()
        minDiff = times[1] - times[0]
        for i in range(len(times) - 1):
            currTime, nextTime = times[i], times[i + 1]
            minDiff = min(minDiff, nextTime - currTime)

        return min(minDiff, times[0] + 1440 - times[-1])

    def standardizeTime(self, hour: int, minute: int) -> int:
        return hour * 60 + minute
