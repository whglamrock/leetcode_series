from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # the actual day number with break days included
        taskToLastExecutedDay = {}
        days = 0
        for task in tasks:
            if task in taskToLastExecutedDay and days - taskToLastExecutedDay[task] <= space + 1:
                waitTime = space + 1 - (days - taskToLastExecutedDay[task])
                days += waitTime
            taskToLastExecutedDay[task] = days
            days += 1

        return days


print(Solution().taskSchedulerII(tasks=[1, 2, 1, 2, 3, 1], space=3))
print(Solution().taskSchedulerII(tasks=[5, 8, 8, 5], space=2))
