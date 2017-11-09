
# n * (n + 1) / 2 <= ans < (n + 1) * (n + 2) / 2
# return n

# O(1) solution. It's a math problem

from math import sqrt

class Solution(object):
    def arrangeCoins(self, n):

        range = int(sqrt(2 * n))
        if (range + 1) * (range + 2) / 2 <= n:
            return range + 1
        elif range * (range + 1) / 2 <= n:
            return range
        else:
            return range - 1