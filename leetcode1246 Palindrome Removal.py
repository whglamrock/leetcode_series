from typing import List

# Intuition: if we know the min removal for nums[i:j], we can calculate it for nums[i - 1:j] and nums[i:j + 1].
# But below cases need to be all considered (it's easy to miss 3), which makes this question a hard level one):
# 1) nums[i - 1] == nums[j + 1];
# 2) nums[i - 1] != nums[j + 1];
# 3) nums[i - 1] along with certain nums[i:x] can make a palindrome, so we need to loop x through [i:j + 1]
class Solution:
    def minimumMoves(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][j] means the min removal needed to empty nums[i:j + 1]
        dp = [[2147483647 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                dp[i][i + 1] = 1
            else:
                dp[i][i + 1] = 2

        # j is the length of the subarray
        for j in range(3, n + 1):
            # i is the starting index
            for i in range(n - j + 1):
                # this is for case 3)
                for k in range(i, i + j - 1):
                    dp[i][i + j - 1] = min(dp[i][i + j - 1], dp[i][k] + dp[k + 1][i + j - 1])
                if nums[i] == nums[i + j - 1]:
                    dp[i][i + j - 1] = min(dp[i][i + j - 1], dp[i + 1][i + j - 2])

        return dp[0][-1]
