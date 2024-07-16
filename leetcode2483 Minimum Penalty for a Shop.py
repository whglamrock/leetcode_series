from collections import defaultdict


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        indexToPrefixN = defaultdict(int)
        indexToPrefixN[-1] = 0
        indexToSuffixY = defaultdict(int)
        indexToSuffixY[n] = 0

        currN = 0
        for i, char in enumerate(customers):
            if char == 'N':
                currN += 1
            indexToPrefixN[i] = currN

        currY = 0
        for i in range(n - 1, -1, -1):
            char = customers[i]
            if char == 'Y':
                currY += 1
            indexToSuffixY[i] = currY

        penalty = [0] * (n + 1)
        for j in range(n + 1):
            penalty[j] = indexToSuffixY[j] + indexToPrefixN[j - 1]

        minPenalty = min(penalty)
        for j in range(n + 1):
            if penalty[j] == minPenalty:
                return j


print(Solution().bestClosingTime("YYNY"))
print(Solution().bestClosingTime("NNNNN"))
print(Solution().bestClosingTime("YYYY"))
