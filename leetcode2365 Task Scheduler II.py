from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # the actual day number with break days included
        days = 0
        taskTypeToLastExecutionTime = {}

        for task in tasks:
            if task in taskTypeToLastExecutionTime and days - taskTypeToLastExecutionTime[task] < space + 1:
                days += space + 1 - (days - taskTypeToLastExecutionTime[task])
                taskTypeToLastExecutionTime[task] = days
            else:
                taskTypeToLastExecutionTime[task] = days
            days += 1

        return days


print(Solution().taskSchedulerII(tasks=[1, 2, 1, 2, 3, 1], space=3))
print(Solution().taskSchedulerII(tasks=[5, 8, 8, 5], space=2))
