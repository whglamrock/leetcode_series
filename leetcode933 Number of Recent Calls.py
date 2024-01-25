from collections import deque

# worst case O(n) solution that runs faster in leetcode. If the time difference between
# consecutive t's is small, it's closer to O(1).
class RecentCounter:
    def __init__(self):
        self.timestamps = deque()

    def ping(self, t: int) -> int:
        while self.timestamps and self.timestamps[0] < t - 3000:
            self.timestamps.popleft()
        self.timestamps.append(t)
        return len(self.timestamps)


'''
# binary solution without popping expired timestamps
class RecentCounter:
    def __init__(self):
        self.timestamps = []

    def ping(self, t: int) -> int:
        self.timestamps.append(t)
        return len(self.timestamps) - self.findIndexBiggerOrEqualThan(self.timestamps, t - 3000)

    def findIndexBiggerOrEqualThan(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] >= target:
                    return m
                else:
                    return -1

            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        return -1
'''