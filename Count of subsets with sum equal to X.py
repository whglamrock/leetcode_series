from typing import List


# question coming from: https://www.1point3acres.com/bbs/thread-1053722-1-1.html
# and geeks for geeks: https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/
class Solution:
    def countSubsetsSumEqualTo(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp[i][j] means the num of subsets in nums[:i] that sum to j
        dp = [[0 for j in range(target + 1)] for i in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j < num:
                    continue

                dp[i][j] += dp[i - 1][j - num]

        return dp[-1][-1]


print(Solution().countSubsetsSumEqualTo([0, 1, 1, 1], 3))
print(Solution().countSubsetsSumEqualTo([1, 1, 1, 1], 1))
print(Solution().countSubsetsSumEqualTo([1, 2, 3, 3], 6))
print(Solution().countSubsetsSumEqualTo([3, 3, 3, 3], 6))
