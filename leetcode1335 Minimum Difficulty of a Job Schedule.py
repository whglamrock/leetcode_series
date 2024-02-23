from functools import lru_cache
from typing import List

# Time complexity of dfs solution can be O(n ^ d) level, but much better with cache. Below is the most practical solution
# to come up with in real interview. Optimal one can be O(n * d), see: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/solutions/490316/java-c-python3-dp-o-nd-solution/
# but it's really not necessary in real interview.
class Solution:
    def __init__(self):
        self.jobDifficulty = []

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        self.jobDifficulty = jobDifficulty
        n = len(jobDifficulty)
        if n < d:
            return -1

        return self.dfs(1, 0, d, n)

    @lru_cache(None)
    def dfs(self, day: int, job: int, d: int, n: int) -> int:
        if job >= n:
            return 0
        if day == d:
            return max(self.jobDifficulty[job:])

        maxDifficultyOfCurrDay = 0
        minDifficulty = 2147483647
        # d - day is days left, which is also the min amount of jobs we have to leave after current day
        for i in range(job, n - (d - day)):
            maxDifficultyOfCurrDay = max(maxDifficultyOfCurrDay, self.jobDifficulty[i])
            minDifficulty = min(minDifficulty, maxDifficultyOfCurrDay + self.dfs(day + 1, i + 1, d, n))

        return minDifficulty


print(Solution().minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
