from collections import deque
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = deque(sorted(tokens))
        score = 0
        maxScore = 0
        while tokens:
            minToken = tokens[0]
            if power >= minToken:
                score += 1
                power -= tokens.popleft()
                maxScore = max(maxScore, score)
            else:
                if score < 1:
                    break
                score -= 1
                power += tokens.pop()

        return maxScore
