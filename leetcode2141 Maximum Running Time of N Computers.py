from typing import List

# the hard part is to figure out that: to check whether batteries can support n computers
# for certain target time, we just need to compare if sum(min(targetTime, batteries[i])) >= targetTime * n
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = 1, sum(batteries) // n
        while l <= r:
            m = (l + r + 1) // 2
            if self.canPossiblySupportTargetTime(m, batteries, n):
                if l == r:
                    return m
                l = m
            else:
                r = m - 1

        return 1

    # assuming swapping batteries optimally and we absolute max out the more powerful batteries,
    # that is, for batteries[i] > target we use "target" number of hours from it.
    # this way we can make sure that if timeCanSupport < target * n the batteries cannot support
    # target time
    def canPossiblySupportTargetTime(self, target: int, batteries: List[int], n: int) -> bool:
        timeCanSupport = 0
        for batteryTime in batteries:
            timeCanSupport += min(target, batteryTime)

        return timeCanSupport >= target * n


print(Solution().maxRunTime(n=2, batteries=[3, 3, 3]))
print(Solution().maxRunTime(n=2, batteries=[1, 1, 1, 1]))
