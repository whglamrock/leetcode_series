from typing import List

# The stupid leetcode gives TLE for below but this solution absolutely acceptable in real interview.
class Solution:
    def __init__(self):
        self.buckets = []
        self.nums = []

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        numSum = sum(nums)
        if numSum % k:
            return False

        self.nums = sorted(nums)[::-1]
        self.buckets = [numSum // k] * k
        return self.dfs(0, k)

    # can't use lru_cache here, to avoid wrong answer
    def dfs(self, i: int, k: int) -> bool:
        if i == len(self.nums):
            return True

        for j in range(k):
            if self.buckets[j] >= self.nums[i]:
                self.buckets[j] -= self.nums[i]
                if self.dfs(i + 1, k):
                    return True
                self.buckets[j] += self.nums[i]

        return False


print(Solution().canPartitionKSubsets([3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932, 4037, 2646, 3871, 269], 5))
