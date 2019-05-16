
# recognizing this can be an NP hard question, gut feeling is to use DP
# divide into 4 conditions

class Solution(object):
    def minSwap(self, A, B):

        n = len(A)
        dp = [[2147483647, 2147483647] for index in xrange(n)]
        dp[0] = [0, 1]

        for i in xrange(1, n):

            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                # no swap on i, no swap on i - 1
                dp[i][0] = min(dp[i][0], dp[i - 1][0])
                # swap on i, swap on i - 1
                dp[i][1] = min(dp[i][1], dp[i - 1][1] + 1)

            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                # swap on i, no swap on i - 1
                dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)
                # no swap on i, swap on i - 1
                dp[i][0] = min(dp[i][0], dp[i - 1][1])

        return min(dp[-1][0], dp[-1][1])



Sol = Solution()
A = [1, 3, 3, 7]
B = [1, 2, 5, 4]
print Sol.minSwap(A, B)
