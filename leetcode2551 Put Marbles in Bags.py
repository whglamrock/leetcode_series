from typing import List

# idea from: https://leetcode.com/problems/put-marbles-in-bags/solutions/3111736/java-c-python-3-approachs-best-o-n/
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) == 1:
            return 0

        maxScore, minScore = weights[0] + weights[-1], weights[0] + weights[-1]
        consecutivePairs = []
        # note that weights[0] and weights[-1] will always be added in score
        # we just need to choose k - 1 cut points, but these points can overlap with
        # weights[0] or weights[-1]
        for i in range(len(weights) - 1):
            consecutivePairs.append(weights[i] + weights[i + 1])
        consecutivePairs.sort()

        maxScore += sum(consecutivePairs[len(consecutivePairs) - k + 1:])
        minScore += sum(consecutivePairs[:k - 1])

        return maxScore - minScore


print(Solution().putMarbles([1, 3, 5, 1], 2))
