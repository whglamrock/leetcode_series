from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            isConsistent = True
            for char in word:
                if char not in allowed:
                    isConsistent = False
                    break

            if isConsistent:
                count += 1

        return count
