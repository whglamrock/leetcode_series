from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        currStart, currEnd = newInterval
        ans = []
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            if end < currStart:
                ans.append([start, end])
            elif currEnd < start:
                ans.append([currStart, currEnd])
                ans.extend(intervals[i:])
                break
            # overlapping
            else:
                currStart = min(currStart, start)
                currEnd = max(currEnd, end)
            i += 1

        if not ans or ans[-1][1] < currStart:
            ans.append([currStart, currEnd])
        return ans


print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
