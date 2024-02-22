from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        m, n = len(processorTime), len(tasks)
        ans = 0
        for i in range(m):
            timeForProcessor = processorTime[i] + tasks[n - 1 - 4 * i]
            ans = max(ans, timeForProcessor)

        return ans
