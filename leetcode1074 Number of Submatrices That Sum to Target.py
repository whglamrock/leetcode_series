from collections import defaultdict
from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rowPrefixSums = []
        for row in matrix:
            prefixSums = []
            for num in row:
                if not prefixSums:
                    prefixSums.append(num)
                else:
                    prefixSums.append(num + prefixSums[-1])
            rowPrefixSums.append(prefixSums)

        m, n = len(matrix), len(matrix[0])
        # for each column pair (i, j), store all possible accumulated sums between [i, j] for the first x number of rows
        sumsBetweenColumns = defaultdict(dict)
        # stores the sub-matrix sum (0, x, i, j) where x keeps growing. The key is (i, j)
        accumulatedSumBetweenColumns = defaultdict(int)
        ans = 0
        for prefixSumsOfEachRow in rowPrefixSums:
            for i in range(n):
                for j in range(i, n):
                    currSubarraySum = prefixSumsOfEachRow[j] - prefixSumsOfEachRow[i - 1] if i > 0 else prefixSumsOfEachRow[j]
                    accumulatedSumBetweenColumns[(i, j)] += currSubarraySum
                    accumulatedSubarraySums = accumulatedSumBetweenColumns[(i, j)]
                    if accumulatedSubarraySums == target:
                        ans += 1
                    if accumulatedSubarraySums - target in sumsBetweenColumns[(i, j)]:
                        ans += sumsBetweenColumns[(i, j)][accumulatedSubarraySums - target]

                    # need to store the count of each accumulatedSubarraySums
                    if accumulatedSubarraySums not in sumsBetweenColumns[(i, j)]:
                        sumsBetweenColumns[(i, j)][accumulatedSubarraySums] = 1
                    else:
                        sumsBetweenColumns[(i, j)][accumulatedSubarraySums] += 1

        return ans
