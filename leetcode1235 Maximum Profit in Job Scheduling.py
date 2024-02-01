from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = []
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key=lambda x: x[1])
        # dp[i] stores the max profit that you can accumulate at endTime[i]
        # p.s. you don't necessarily have to take job[i]
        dp = [0] * n
        dp[0] = jobs[0][2]

        for i in range(1, n):
            maxIndexOfEarlierJob = self.findMaxIndexSmallerOrEqual(jobs, jobs[i][0], i - 1)
            if maxIndexOfEarlierJob == -1:
                dp[i] = max(dp[i - 1], jobs[i][2])
            else:
                dp[i] = max(dp[i - 1], dp[maxIndexOfEarlierJob] + jobs[i][2])

        return dp[-1]

    def findMaxIndexSmallerOrEqual(self, jobs: List[List[int]], target: int, r: int) -> int:
        l = 0
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if jobs[m][1] <= target:
                    return m
                else:
                    return -1
            if jobs[m][1] <= target:
                l = m
            else:
                r = m - 1

        return -1


print(Solution().jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]))
print(Solution().jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]))
print(Solution().jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))
