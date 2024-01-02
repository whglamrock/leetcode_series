from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key=lambda x: x[1])
        endTime.sort()

        # dp[i] stores the max profit that you can accumulate at endTIme[i]
        # p.s. you don't necessarily have to take job[i]
        dp = [0] * n
        dp[0] = jobs[0][2]
        for i in range(1, n):
            maxIndexOfJobEarlier = self.findMaxIndexEqualOrLessThanTarget(endTime, jobs[i][0], 0, i - 1)
            if maxIndexOfJobEarlier != -1:
                dp[i] = max(jobs[i][2] + dp[maxIndexOfJobEarlier], dp[i - 1])
            # can't even find any job earlier
            else:
                dp[i] = max(jobs[i][2], dp[i - 1])

        return dp[-1]

    def findMaxIndexEqualOrLessThanTarget(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l <= r:
            if l == r:
                if nums[l] > target:
                    return -1
                else:
                    return l
            m = (l + r + 1) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m

        return -1


print(Solution().jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]))
print(Solution().jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]))
print(Solution().jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))
