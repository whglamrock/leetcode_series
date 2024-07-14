from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cards = cardPoints[len(cardPoints) - k:len(cardPoints)] + cardPoints[:k]
        maxSum = sum(cards[:k])

        currSum = maxSum
        for i in range(k, len(cards)):
            currSum = currSum - cards[i - k] + cards[i]
            maxSum = max(maxSum, currSum)

        return maxSum
