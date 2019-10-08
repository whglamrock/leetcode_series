
from heapq import *

# it's natural to think of a priorityQueue solution.

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # sort the array by start time first
        intervals.sort()
        q = []
        heapify(q)

        ans = 0
        for i, j in intervals:
            # in priorityQueue we wanna sort by end time
            heappush(q, j)
            # in real interview we need to confirm whether it should be '<=' or '<'
            while q and q[0] <= i:
                heappop(q)
            ans = max(ans, len(q))

        return ans



print Solution().minMeetingRooms([[13, 15], [1, 13]])
print Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]])