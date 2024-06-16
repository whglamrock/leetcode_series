from collections import deque
from typing import List


# Simply reverse the process:
# 17
# 13, 17
# 13, 17 -> 17, 13 -> 11, 17, 13
# 11, 17, 13 -> 13, 11, 17 -> 7, 13, 11, 17
# 7, 13, 11, 17 -> 17, 7, 13, 11 -> 5, 17, 7, 13, 11
# 5, 17, 7, 13, 11 -> 11, 5, 17, 7, 13 -> 3, 11, 5, 17, 7, 13
# 3, 11, 5, 17, 7, 13 -> 13, 3, 11, 5, 17, 7 -> 2, 13, 3, 11, 5, 17, 7
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque()
        for num in sorted(deck)[::-1]:
            if q:
                q.appendleft(q.pop())
            q.appendleft(num)

        return list(q)
