

# see solid proof for optimality of greedy algorithm: https://leetcode.com/problems/couples-holding-hands/discuss/113369/Formal-proof-of-the-optimality-of-greedy-algorithm

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        if not row:
            return 0

        valToIndex = {}
        for i, val in enumerate(row):
            valToIndex[val] = i

        count = 0
        for i in xrange(0, len(row), 2):
            val = row[i]
            valToPair = val + 1 if val % 2 == 0 else val - 1
            if row[i + 1] != valToPair:
                self.swapPeople(i + 1, row, valToPair, valToIndex)
                count += 1

        return count

    # indexToSwap is i + 1, valToPair is expected value at i + 1
    def swapPeople(self, indexToSwap, row, valToPair, valToIndex):
        # tmp is the value that doesn't pair with row[i] and needs to swapped out
        tmp = row[indexToSwap]
        indexToSwapWith = valToIndex[valToPair]

        # do the swap in valToIndex map
        valToIndex[valToPair] = indexToSwap
        valToIndex[tmp] = indexToSwapWith

        # do the swap in row
        row[indexToSwap] = valToPair
        row[indexToSwapWith] = tmp



print Solution().minSwapsCouples([0, 5, 2, 4, 1, 3])