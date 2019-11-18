
# The intervals is sorted and non-overlapping
# binary search O(N) solution because insert item takes O(N) anyways

from bisect import bisect_left, bisect_right

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        flattenedIntervals = []
        for interval in intervals:
            flattenedIntervals.append(interval[0])
            flattenedIntervals.append(interval[1])

        i = bisect_left(flattenedIntervals, newInterval[0])
        j = bisect_right(flattenedIntervals, newInterval[1])
        flattenedIntervals[i:j] = [newInterval[0]] * (i % 2 == 0) + [newInterval[1]] * (j % 2 == 0)

        intervals = []
        for i in xrange(0, len(flattenedIntervals) - 1, 2):
            intervals.append([flattenedIntervals[i], flattenedIntervals[i + 1]])

        return intervals



print Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])