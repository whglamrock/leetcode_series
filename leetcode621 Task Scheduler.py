from collections import Counter
from heapq import *
from typing import List


# use a min heap to store the nextExecutionTime, number of tasks left. Try to execute the task with min
# nextExecutionTime and most task count. If nextExecutionTime is still in future, we idle.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        pq = []
        for task, count in taskCount.items():
            heappush(pq, [0, -count])

        intervals = 0
        while pq:
            if pq[0][0] > intervals:
                intervals += 1
                continue

            executionTime, count = heappop(pq)
            count = -count
            count -= 1
            intervals += 1

            if count == 0:
                continue
            heappush(pq, [executionTime + n + 1, -count])

        return intervals
