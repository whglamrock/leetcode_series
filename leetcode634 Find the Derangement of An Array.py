
# it's actually a hard level DP problem.
# See explanation: https://leetcode.com/problems/find-the-derangement-of-an-array/solutions/104981/if-you-don-t-understand/comments/806040
class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1

        mod = 10 ** 9 + 7
        prevPrev = 0
        prev = 1
        curr = 0
        for i in range(3, n + 1):
            curr = (i - 1) * (prevPrev + prev)
            curr %= mod
            prevPrev = prev
            prev = curr

        return curr
