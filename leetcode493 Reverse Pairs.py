
# same ranking idea as lc315.

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newNums = sorted(set(nums + [2 * x for x in nums]))
        ranks = {num: rank + 1 for rank, num in enumerate(newNums)}
        bit = [0] * (len(newNums) + 1)

        ans = 0
        for num in nums[::-1]:
            ans += self.queryBIT(bit, ranks[num] - 1)
            # this is the key for redefining the question into a BIT question
            self.updateBIT(bit, ranks[num * 2])

        return ans

    def queryBIT(self, bit, i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= (i & -i)
        return s

    def updateBIT(self, bit, i):
        while i < len(bit):
            bit[i] += 1
            i += (i & -i)
