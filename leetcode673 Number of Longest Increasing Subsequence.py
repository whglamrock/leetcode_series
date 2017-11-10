
# O(N^2) solution

class Solution(object):
    def findNumberOfLIS(self, nums):

        if not nums:
            return 0

        n = len(nums)
        # dp[i] stores the length and number of longest sub-sequence ends with nums[i]
        dp = [[1, 0] for _ in xrange(n)]
        dp[0][1] = 1
        max_len = 1

        for i, num in enumerate(nums):
            prev_longest = 0
            # find the length of previous longest sub-sequence
            for j in xrange(i):
                if nums[j] < num:
                    prev_longest = max(prev_longest, dp[j][0])
            dp[i][0] = prev_longest + 1
            # if prev_longest == 0 then no nums[j] < num
            dp[i][1] = 1 if prev_longest == 0 else 0
            for j in xrange(i):
                if dp[j][0] == prev_longest and nums[j] < num:
                    dp[i][1] += dp[j][1]
            max_len = max(max_len, dp[i][0])

        ans = 0
        for length, num_of_subseq in dp:
            if length == max_len:
                ans += num_of_subseq

        return ans
