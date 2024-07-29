
# O(n) time solution. The O(1) space solution probably requires bit manipulation.
class Solution:
    def partitionString(self, s: str) -> int:
        window = {}
        l, n = 0, len(s)
        endIndexToNonRepeatStart = [0] * n
        for r, char in enumerate(s):
            if char in window:
                lastIndex = window[char]
                while l <= lastIndex:
                    del window[s[l]]
                    l += 1

            window[char] = r
            endIndexToNonRepeatStart[r] = l

        dp = [i + 1 for i in range(n)]
        for i in range(1, n):
            if endIndexToNonRepeatStart[i] == 0:
                dp[i] = 1
                continue

            # j is the end index of the previous substring, so it can be as small as endIndexToNonRepeatStart[i] - 1
            # the number of below for loop will be <= 26
            for j in range(i - 1, endIndexToNonRepeatStart[i] - 2, -1):
                dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]
