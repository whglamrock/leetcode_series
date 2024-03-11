class Solution:
    def numWays(self, s: str) -> int:
        oneIndexes = []
        for i, digit in enumerate(s):
            if digit == '1':
                oneIndexes.append(i)

        if len(oneIndexes) % 3:
            return 0

        if oneIndexes:
            numOfWaysToBuildS1 = oneIndexes[len(oneIndexes) // 3] - oneIndexes[len(oneIndexes) // 3 - 1]
            numOfWaysToBuildS2 = oneIndexes[len(oneIndexes) // 3 * 2] - oneIndexes[len(oneIndexes) // 3 * 2 - 1]
            return numOfWaysToBuildS1 * numOfWaysToBuildS2 % (10 ** 9 + 7)

        ans = 0
        n = len(s)
        # i is the starting position
        for i in range(n - 2):
            # the end position of the 2nd string can be i + 1 to n - 2
            ans += (n - 2) - (i + 1) + 1

        return ans % (10 ** 9 + 7)
