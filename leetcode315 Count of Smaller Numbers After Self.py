
from collections import deque

# redefine the question to a binary index tree question:
    # every number has a rank: the count of numbers smaller than ranks(4) = count of numbers at ranks(3)
    # + count of numbers at ranks(2) + count of numbers at ranks(1).
# => this is essentially queryBIT(3).

# Naturally we make ranks(i) = 1.

# if we do this in reverse order, we can get the answer

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)

        # BIT is non-0 index based array because we need to perform bit operation on index
        ranks = {num: rank + 1 for rank, num in enumerate(sorted(nums))}
        bit = [0] * (n + 1)

        res = deque()
        for num in nums[::-1]:
            # we want the sum of counts of lower rank numbers and
                # at this point only the numbers on the right of num were added to BIT
            # we need smaller numbers so use rank - 1 (BIT "prefix sum" is inclusive)
            count = self.queryBIT(bit, ranks[num] - 1)
            res.appendleft(count)
            self.updateBIT(bit, ranks[num])

        return res

    # no diff in input here because we always add 1
    def updateBIT(self, bit, i):
        while i < len(bit):
            bit[i] += 1
            i += (i & -i)

    def queryBIT(self, bit, i):
        ans = 0
        while i > 0:
            ans += bit[i]
            i -= (i & -i)
        return ans



print Solution().countSmaller([5, 6, 2, 1, 3, 4, 7, 8, 10])
