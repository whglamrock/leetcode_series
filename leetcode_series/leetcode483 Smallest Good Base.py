
# Since we have n = k ^ m + k ^ (m - 1) + ... + k + 1, to find the smallest k
#   is to find the biggest m.
#   According to geometric progression, n = (1 - k ^ (m + 1)) / (1 - k).
#   Since k >= 2 (as a base, k has to be at lease 2),
#   (k ^ (m + 1) - 1) / (k - 1) <= (k ^ (m + 1) - 1) / (2 - 1)
#   = k ^ (m + 1) - 1 < k ^ (m + 1)
#   Thus, k ^ m < n < k ^ (m + 1), logk(k ^ m) < logk(n) < logk(k ^ (m + 1)),
#   m < logk(n) < m + 1.
# CONCLUSION: m = int(logk(n)), and we only needa check
#   if n == (1 - k ^ (m + 1)) / (1 - k)

# Initiating k as 2, m can be at most log2(n), then use this range to do linear
#   search.
# P.S.: technically this question is not a binary search but a math problem
# Regarding the two or more "**"s in a row: with a ** b ** c, Python will calculate
#   (b ** c) first, then calculate a ** (b ** c). All "**"s afterwards will be ignored (like
#   a ** b ** c ** d ** e, the result == a ** b ** c).

import math

class Solution(object):
    def smallestGoodBase(self, n):

        # don't forget n is a string
        n = int(n)
        max_m = int(math.log(n, 2))
        # the m can be as small as 2

        for m in xrange(max_m, 1, -1):
            # use float for "/" to get a float number, or the float division "/" gives an int
            k = int(n ** (1.0 / m))    # P.S., k == int(n ** m ** -1)
            if n == (1 - k ** (m + 1)) / (1 - k):   # don't use "//" here
                return str(k)

        return str(n - 1)



Sol = Solution()
print Sol.smallestGoodBase('4681')

